/*
    Spreadsheet.java
    
    Spreadsheet wrapper and controller class. Has Cell class objects held in
    2D array of cells based on input row and columns. Also manages the parsing
    of inter-cell values.
*/

import java.util.*;
import java.util.regex.*;

public class Spreadsheet {
    private int row, col;
    private Cell[][] sheet;
    
    // Default Constructor
    // Default spreadsheet size is 0,0
    public Spreadsheet() {
        this.row = this.col = 0;
    }
    
    // Parameterized Constructor
    // Takes in the rows and columns to form the basis of the spreadsheet
    // Default size is 0, 0
    public Spreadsheet(int rowIN, int colIN) {
        if(rowIN > 0 && colIN > 0) {
            this.row = rowIN;
            this.col = colIN;
            
            this.sheet = new Cell[rowIN][colIN];
        } else {
            this.row = 0;
            this.col = 0;
        }
    }
    
    // Getters and Setters
    public int getRow() {
        return this.row;
    }
    
    public int getCol() {
        return this.col;
    }
    
    public Cell[][] getSheet() {
        return this.sheet;
    }
    
    // STUB : Maybe, add growing and shrinking by changing cell sizes, later
    
    
    // Methods
    
    // STUB : Growing/shrinking cell sizes
    // expandSheet
    // If adding growing/shrinking cell sizes, later
    // STUB : Growing/shrinking cell sizes
    // shrinkSheet
    
    // addCell
    // Adds the incoming cell to the spreadsheet if the cell paramters are 
    // safe and recalculates the sheet to account for the change
    // O(row*col * (strlenA + strlenB) + strlen) as each insert reevaluates the spreadsheet
    // and concatenating strings in finding recursed cells
    public boolean addCell(Cell cell) {
        // Cannot add cells outside of bounds
        if(cell.getRow() >= this.row || cell.getRow() < 0 ||
            cell.getCol() >= this.col || cell.getCol() < 0) {
            return false;
        }
        
        // Insert the new cell
        this.sheet[cell.getRow()][cell.getCol()] = cell;
        
        // Recalculate all the cells that may have depended on the old one
        calculateAllCellValues();
        
        return true;
    }
    
    // calculateCellValue
    // Calculates the cell's value by referencing all legal entries so far
    // and replacing column-indexed values with their numeric calculations
    // Returns success or failure if cannot proceed at time of call
    // O(replacements * (strlenA + strlenB) + strlen) as each insert reevaluates the spreadsheet
    // and concatenating strings in finding recursed cells plus evaluating terminal strings
    // Space: O(2*replacements + strlen) (and probably some junk that could be cleaned)
    public boolean calculateCellValue(int cellRow, int cellCol) {
        // Cannot add cells outside of bounds
        if(cellRow >= this.row || cellRow < 0 || cellCol >= this.col || cellCol < 0) {
            return false;
        }
        
        Cell holdCell = this.sheet[cellRow][cellCol];
        String holdInput = holdCell.getInput();
        
        // Regular Expressions for fast matching of column-major notation
        String regexPattern = 	"[A-Z]{1}[1-9]+";
        Pattern pattern = Pattern.compile(regexPattern);
        Matcher matcher = pattern.matcher(holdInput);
        ArrayList<Integer> subCellRows = new ArrayList<Integer>();
        ArrayList<Integer> subCellCols = new ArrayList<Integer>();
        
        // Get each of the starting positions of the cell notations
        while(matcher.find()) {
            subCellCols.add(holdInput.charAt(matcher.start()) - 'A');
            subCellRows.add(holdInput.charAt(matcher.start() + 1) - '1');
        }
        
        // If no matches found, can process the string within the cell
        if(subCellCols.size() == 0) {
            int newValue = holdCell.calculateStringValue(holdInput);
            
            if(newValue >= 0) {
                this.sheet[cellRow][cellCol].setValue(newValue);
            }
            
            return true;
        }
        
        // Otherwise, need to go through and find those cells which have values
        // and replace in the string
        // STUB : This could probably be moved out to a helper method
        while(!subCellCols.isEmpty()) {
            int holdCol = subCellCols.remove(0);
            int holdRow = subCellRows.remove(0);
            String replacer = "" + (char)(holdCol + 'A') + (char)(holdRow + '1');
            
            // Check for a safe cell and get its value
            if(holdCol >= 0 && holdCol < this.col && holdRow >= 0 && holdRow < this.row) {
                // A found value should be substituted back into the string
                if(this.sheet[holdRow][holdCol] != null) {
                    String testString = this.sheet[holdRow][holdCol].getInput();
                    holdInput = holdInput.replaceAll(replacer, testString);
                } else {
                    return false;
                }
            }
        }
        
        // Put the input string back into the Cell (calling calculator)
        this.sheet[cellRow][cellCol].setInput(holdInput);
        
        // String was successful if substituted values came back with a success
        if(this.sheet[cellRow][cellCol].getValue() >= 0) {
            return true;
        }
        
        // Otherwise, failure until next iteration
        return false;
    }
    
    // calculateAllCellValues
    // O(row*col * (strlenA + strlenB) + strlen) as each insert reevaluates the spreadsheet
    // and concatenating strings in finding recursed cells
    public boolean calculateAllCellValues() {
        ArrayList<Cell> postRefs = new ArrayList<Cell>();
        int probeDepth = this.row;
        
        // Go through the cells and calculate the values
        for(int index = 0; index < this.row; index++) {
            for(int column = 0; column < this.col; column++) {
                // Gather up those cells which didn't immediately parse
                if(this.sheet[index][column] != null && !calculateCellValue(index, column)) {
                    postRefs.add(this.sheet[index][column]);
                }
            }
        }
        
        while(!postRefs.isEmpty() && probeDepth > 0) {
            Cell holdCell = postRefs.remove(0);
            
            if(!calculateCellValue(holdCell.getRow(), holdCell.getCol())) {
                postRefs.add(holdCell);
                probeDepth--;
            }
        }
        
        return true;
    }
    
    // printSpreadsheet
    // Prints the spreadsheet's values out in a comma-separated matrix
    // O(row * col)
    public void printSpreadsheet() {
        // Go over each cell
        for(int rowIndex = 0; rowIndex < this.row; rowIndex++) {
            String rowString = "";
            
            for(int colIndex = 0; colIndex < this.col; colIndex++) {
                if(this.sheet[rowIndex][colIndex] != null) {
                    int value = this.sheet[rowIndex][colIndex].getValue();
                    if(value >= 0) {
                        if(colIndex > 0) {
                            rowString = rowString + ", " + value;
                        } else {
                            rowString = rowString + value;
                        }
                    } else {
                        if(colIndex > 0) {
                            rowString = rowString + ", #REF!";
                        } else {
                            rowString = rowString + "#REF!";
                        }
                    }
                } else {
                    rowString = rowString + " null ";
                }
            }
        
            System.out.println(rowString);
        }
    }
}