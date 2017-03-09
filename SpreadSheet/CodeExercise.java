/*
    CodeExercise.java
    
    Coding assignment for interview on Java. Emulates a simplified spreadsheet
    using formulae in Reverse Polish Notation and prints out the results.
    
    Brittany McGarr
    February 2017
*/

import java.util.*;
import java.io.*;

public class CodeExercise {
    
    // Main program for running the program on test data
    public static void main(String[] args) {
        // STUB : Compilation tests
        /*
            if(testCells()) {
                System.out.println("Cell tests passed.\n");
            } else {
                System.out.println("ERROR: Some tests did not pass for Cell class.\n");
            }
        */
        
        for(int index = 0; index < 5; index++) {
            System.out.println("Testing data file " + index + " : ");
            testSpreadsheet("data_" + index + ".txt");
            System.out.println("\n");
        }
        
    }
    
    // Test the Cells
    public static boolean testCells() {
        boolean passed = true;
        Cell testCellA = new Cell(1, 1, "2 3 +"); // value: 5
        Cell testCellB = new Cell(1, 2, "3 12 + 4 +"); // value: 19
        Cell testCellC = new Cell(1, 3, "1 2 3"); // value: -1
        Cell testCellD = new Cell(1, 4, "1 2 3 * +"); // value: 7
        
        System.out.println("Testing Cell A: (2 3 +) == 5");
        System.out.println("" + testCellA.getValue() + "\n");
        passed = passed && (testCellA.getValue() == 5) ? true : false;
        
        System.out.println("Testing Cell B: (3 12 + 4 +) == 19");
        System.out.println("" + testCellB.getValue() + "\n");
        passed = passed && (testCellB.getValue() == 19) ? true : false;
        
        System.out.println("Testing Cell C: (1 2 3) *Error*");
        System.out.println("" + testCellC.getValue() + "\n");
        passed = passed && (testCellC.getValue() == -1) ? true : false;
        
        System.out.println("Testing Cell D: (1 2 3 * +) == 7");
        System.out.println("" + testCellD.getValue() + "\n");
        passed = passed && (testCellD.getValue() == 7) ? true : false;
        
        return passed;
    }
    
    // Testing the spreadsheet against file data
    public static boolean testSpreadsheet(String fileName) {
        boolean passed = true;
        int rows, cols;
        int rowCount = 0, colCount = 0;
        String hold;
        
        File file = new File(fileName);
        FileInputStream fileIN = null;
        
        try {
            fileIN = new FileInputStream(file);
        } catch (IOException except) {
			except.printStackTrace();
			return false;
		}
		
		Scanner scanner = new Scanner(fileIN);
        hold = scanner.nextLine();
        String[] parameters = hold.split(",");
        
        rows = Integer.parseInt(parameters[0]);
        cols = Integer.parseInt(parameters[1]);
        
        Spreadsheet spreadsheet = new Spreadsheet(rows, cols);
        
        while(scanner.hasNext()) {
            hold = scanner.nextLine();
            String[] inputs = hold.split(",");
            
            for(String input : inputs) {
                Cell holdCell = new Cell(rowCount, colCount, input);
                spreadsheet.addCell(holdCell);
                
                colCount++;
            }
            
            colCount = 0;
            rowCount++;
        }
        
        spreadsheet.printSpreadsheet();
        
        
        return passed;
    }
}