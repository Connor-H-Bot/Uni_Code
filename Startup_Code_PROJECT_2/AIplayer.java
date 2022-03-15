import java.util.*;
import javax.swing.Box;
import java.util.Random;
/**
 * Implments a simple AI player to 
 * automatically contol the tiger moves
 *
 * @Student 1 Name: Connor Harris
 * @Student 1 Number: 23208009
 * 
 * @Student 2 Name: Kai Stewart-Wynne
 * @Student 2 Number: 23095602
 */

public class AIplayer
{
    private Random rn; // for random tiger or location selection
    private GameRules rul; // an instance of GameRules to check for legal moves
    private boolean[] tigerLocs; // bool array for tigerlocation. TRUE if tiger poppulates  
    private int ntigers; // number of tigers placed
    /**
     * Constructor for objects of class AIplayer.
     * Initializes instance variables.
     */
    public AIplayer()
    {
        rn = new Random();
        rul = new GameRules();
        tigerLocs = new boolean[24];
        for (int i=0; i<tigerLocs.length; i++){ 
            tigerLocs[i] = false; // initialises array with all false values
        }
        ntigers = 0;    
    }
    
    /**
     * Generates random integer between 0-24. Used for AI placement during phase 1. 
     */
    public int randomNumberGen()
    {
        int randomNumber = rn.nextInt(24);
        return randomNumber;
    }
    
    /**
     * Checks if the location is populated by a tiger
     */
    public boolean isTiger(int i) 
    {
        if (tigerLocs[i] == true){ 
            return true;
        }
            else {    
            return false;
        }
    }
    
    /**
     * Place tiger in a random vacant location on the Board
     * Update the board, the tiger count and tigerLocs.
     */
    public void placeTiger(Board bd)
    {
        int i = this.randomNumberGen();  //rng to place tiger at loc
        while (bd.isVacant(i) == false){ //checks if location is vacant
            i = 0;
            i = this.randomNumberGen(); //resets the random int and repeats previous line to test vacancy
        }
        bd.setTiger(i);      //statement to execute when board piece is free
        ntigers += 1;        //increment tiger counter
        tigerLocs[i] = true; //update tiger location on array
    }
    
    /**
     * Returns number of tigers
     */
    public int getnTigers()
    {
        return ntigers;
    }
    
    /**
     * Method not used
     */
    public int makeAmove(Board bd)
    {
        if (eatGoat(bd))  return 1; // did eat a goat
        else if (simpleMove(bd)) return 0; // made a simple move
        else return -1; // could not move
    }
    
    /**
     * Method not used
     */
    private boolean simpleMove(Board bd)
    {
        //TODO 21
        return false; 
    }
    
    /**
     * Method not used
     */
    private boolean eatGoat(Board bd)
    {
        //TODO 22        
        return false;
    }
}
