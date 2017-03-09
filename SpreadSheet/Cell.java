/*
    Cell.java

    Spreadsheet cell class for storing the input, integer data.
    
    ** IF Time: Extend with generics for float/double/long, and String 
    concatenation (+) and maybe, intersection with *?
*/

import java.util.*;

public class Cell {
    private int row, col;
    private String name, input;
    private int value;
    
    // Default Constructor
    // Given no parameters, a blank cell with -1 value is added in
    public Cell() {
        this.row = this.col = this.value = -1;
        this.name = this.input = "";
    }
    
    // Parameterized Constructor
    // Takes in the known cell data and makes a best-effort to get value
    // Default value will be -1 for strings that cannot be parsed at entry
    public Cell(int rowIN, int colIN, String inputIN) {
        this.row = rowIN;
        this.col = colIN;
        
        // Name is assuming column-major notation (e.g. "D2")
        this.name = "" + (colIN + 'A') + rowIN;
        
        this.input = inputIN;
        
        // Get the input string and see if an integer is present
        try {
            this.value = Integer.parseInt(inputIN);
            
            if(this.value < 0) {
                this.input = "#REF!";
            }
        } catch(NumberFormatException except) {
            // Not in integer format, so must be equation
            this.value = calculateStringValue(inputIN);
        }
    }
    
    // Getters and Setters
    public int getRow() {
        return this.row;
    }
    
    public int getCol() {
        return this.col;
    }
    
    public String getName() {
        return this.name;
    }
    
    public String getInput() {
        return this.input;
    }
    
    public int getValue() {
        return this.value;
    }
    
    // Update naming convention for changed rows/columns
    public void setRow(int rowIN) {
        this.row = rowIN;
        updateName();
    }
    
    public void setCol(int colIN) {
        this.col = colIN;
        updateName();
    }
    
    // Allow update of input string and calculation of new value
    public void setInput(String incoming) {
        this.input = incoming;
        
        // Get the input string and see if an integer is present
        try {
            this.value = Integer.parseInt(incoming);
            
            if(this.value < 0) {
                this.input = "#REF!";
            }
        } catch(NumberFormatException except) {
            // Not in integer format, so must be equation
            this.value = calculateStringValue(incoming);
        }
    }
    
    // Allow update of value with new input string
    public void setValue(int valueIN) {
        this.value = valueIN;
        
        if(this.value < 0) {
            this.input = "#REF!";
        } else {
            this.input = "" + valueIN;
        }
    }
    
    // Methods
    
    // updateName
    // Updates the name based on the current values of the row and column,
    // using column-major convention
    private void updateName() {
        this.name = "" + (this.col + 'A') + this.row;
    }
    
    // calculateStringValue
    // Takes the String input and parses it for farthest, reachable value
    // Spreadsheet must handle outer-communication of cells, but can handle
    // expressions within the cell. e.g. "2 4 + 3 +"
    // Returns -1 as value if unable to proceed
    // O(strlen) as each is handled along the string
    // Space: O(strlen + consts) for the stack.
    public int calculateStringValue(String incoming) {
        int hold = 0, result = -1;
        Stack<Integer> inputs = new Stack<Integer>();
        
        // For each character in the input,
        for(int index = 0; index < incoming.length() && incoming.charAt(index) != '\n'; index++) {
            char holdChar = incoming.charAt(index);
            
            // Characters >= 65 (Dec) are letters (including lower-case)
            if(holdChar >= 'A' && holdChar != '\n') {
                // Characters indicate external cells, and the function
                // Cannot be calculated, yet
                this.value = -1;
                return -1;
            }
            
            // Characters 42 '*' and 43 '+' indicate operation
            if(holdChar == '*' || holdChar == '+') {
                // Operands pull the last two values on the stack,
                if(inputs.size() >= 2) {
                    int a = inputs.pop();
                    int b = inputs.pop();
                    
                    // Operate on them,
                    if(holdChar == '*') {
                        result = a * b;
                    } else {
                        result = a + b;
                    }
                    
                    // And push the result back on the stack
                    inputs.push(result);
                } else {
                    this.value = -1;
                    return -1;
                }
            }
            
            // Otherwise, numbers in range of 48 '0' to 57 '9' must be extended
            if(holdChar >= '0' && holdChar <= '9') {
                hold = 0;
                
                while(holdChar >= '0' && holdChar <= '9') {
                    // Another digit for the value is discovered, move the last values
                    // over and add the new
                    hold = hold * 10 + (holdChar - '0');
                    
                    // We will still be moving along the string, so push forward and
                    // get the next character for the next check in the loop
                    index++;
                    
                    if(index < incoming.length()) {
                        holdChar = incoming.charAt(index);
                    } else {
                        holdChar = ' ';
                    }
                }
                
                // Add the new value into the stack
                inputs.push(hold);
            }
        }
        
        // Check that the stack has only one value left, the result
        // Any other values indicate an error on the input. e.g. "9 2"
        if(inputs.size() == 1) {
            this.value = inputs.pop();
            
            return this.value;
        } else {
            this.value = -1;
            return -1;
        }
    }
}