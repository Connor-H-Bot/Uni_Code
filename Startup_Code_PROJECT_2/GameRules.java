import java.util.ArrayList;
//import java.util.stream.Stream;
/**
 * Maintains game rules. Checks if a move is legal.
 * It also maintains move turns and the game stage.
 *
 * @Student 1 Name: Connor Harris
 * @Student 1 Number: 23208009
 * 
 * @Student 2 Name: Kai Stewart-Wynne
 * @Student 2 Number: 23095602
 */
public class GameRules
{
    // Instance variables to maintain whose move it is
    private boolean moveStage; 
    private boolean goatsTurn;
    private int numGoats; //the number of goats on the board
    private int numTigers; //the number of tigers on the board
    private final int MAXGOATS = 12; 
    public int legalEatsIndex = 0;
    
    // list of all legal moves legalMoves[0] is {1,3,9} which means a piece from [0] can move to 
    // [1],[3] or [9]. legalMoves[1] is {0,2,4} meaning a piece from [1] can move to [0],[2] or [4]
    public final int[][] legalMoves = {{1,3,9},{0,2,4},{1,5,14},{0,4,6,10},{1,3,5,7},{2,4,8,13},
    {3,7,11},{4,6,8},{5,7,12},{0,10,21},{3,9,11,18},{6,10,15},{8,13,17},{5,12,14,20},{2,13,23},
    {11,16,18},{15,17,19},{12,16,20},{10,15,19,21},{16,18,20,22},{13,17,19,23},{9,18,22},{19,21,23},
    {14,20,22}};     
    
    //list of all legal eat moves by tigers e.g. legalEats[0] means that a tiger at [0] can 
    // eat a goat at [1] and land in [2] (there has to be a goat at [1] and [2] must be vacant)
    // tiger at [0] can also eat a goat at [9] and jump to 21 OR eat a goat at [3] and jump to [6]
    // legalEats[4]={} is empty meaning that at tiger at [4] has no options
    private final int[][] legalEats = {{1,2, 9,21, 3,6}, {4,7}, {1,0, 5,8, 14,23}, {4,5, 10,18},{},
    {4,3, 13,20}, {3,0, 7,8, 11,15}, {4,1}, {5,2, 7,6, 12,17}, {10,11},{}, {10,9}, {13,14},{},
    {13,12}, {11,6, 16,17, 18,21}, {19,22}, {12,8, 16,15, 20,23}, {10,3, 19,20},{}, {13,5, 19,18},
    {9,0, 18,15, 22,23}, {19,16}, {14,2, 20,17, 22,21}};                              

    /**
     * Constructor for objects of class GameRules
     */
    public GameRules()
    {              
        moveStage = false;
        goatsTurn = true;
        numGoats = 0;
        numTigers = 0;
    }       
    
    /**
     * returns moveStage
     */
    public boolean isMoveStage()
    {
        return moveStage;
    }
    
    /**
     * returns true or false depending on whether its goats turn or not. 
     */
    public boolean isGoatsTurn()
    {
        return goatsTurn;
    }    
    
    /**
     * Adds (+1 or -1) to goat numbers.
     * Changes the goatsTurn and moveStage as per rules.
     */
    public void addGoat(int n)
    {
        if ((this.numGoats != MAXGOATS) && (this.numTigers != 3) && (moveStage == false)){ //continue to add goat if vals arent maxxed
            this.numGoats += n;
        } 
        if ((this.numGoats == MAXGOATS) && (this.numTigers == 3) && (this.moveStage == false)) { //checks if goats & tigers are maxx'd
            this.moveStage = true; //changes game to phase 2 when at max
        }
        if (moveStage == false){ //checks whos turn it is during phase 1
            if ((numGoats != 4) && (numGoats != 8) && (numGoats != MAXGOATS)){ //check if goat turn
                goatsTurn = true; 
                }
                else { //on the 4th, 8th, and 12th goat placement this will change turns to tigers
                goatsTurn = false;
                }
        } else { //During moveStage the goat count can only go down. If it has just gone down it was tigers move
            this.numGoats -= 1;
        }
    }
    
    public void changeMoveStage() 
    {
        if (this.moveStage == false) {
            this.moveStage = true;
        }
    }
    
    /**
     * returns number of goats
     */
    public int getNumGoats()
    {
        return numGoats;
    }
    
    /**
     * returns number of tigers
     */
    public int getNumTigers()
    {
        return numTigers;
    }
    
    /**
     * increments tigers and gives turn back to goats
     */
    public void incrTigers()
    {
        this.numTigers += 1;
        this.goatsTurn = true;
    }
   
    /**
     * Mutator method to change whos turn it is
     */
    public void changeTurn() { 
        if (this.goatsTurn == true) {
            this.goatsTurn = false;
        } else {
            this.goatsTurn = true;
        }
    }
    
    /**
     * Returns the nearest valid location (0-23) on the board to the x,y mouse click.
     * If the click is close enough to a valid location on the board, return 
     * that location, otherwise return -1 (when the click is not close to any location).
     * Choose a threshold for proximity of click based on bkSize.
     */    
    public int nearestLoc(int x, int y, int bkSize)
    {
        int loc = -1;
        int limit = bkSize*4; //variable for the maximum distance
        for (int i = 0; i<24; i++){
            int distance = 0;
            int xDistance = x - (bkSize*GameViewer.locs[i][0]); // distance to nearest location in the x axis
            int yDistance = y - (bkSize*GameViewer.locs[i][1]);// distance to nearest location in the y axis
            xDistance *= xDistance;
            yDistance *= yDistance; //squared to calculate distance
            distance = xDistance + yDistance;
            distance = distance^(1/2);
            if (distance < limit){
                loc = i;
            }
        }
        return loc;    
    }
    
    /**
     * Returns true iff a move from location a to b is legal, otherwise returns false.
     * For example: a,b = 1,2 -> true; 1,3 -> false; 20,17 -> true. 
     */
    public boolean isLegalMove(int a, int b)
    {  
        int i = 0;                   //instance variable for loop to run through array
        boolean legalStatus = false; //default value
        while ((b != legalMoves[a] [i]) && (i < legalMoves[a].length - 1)) {  //a = goatLoc, b = goatDestination, i = sifting number
            i += 1;                  //increments i by one to keep going through the 2d array
        } 
        if (b == legalMoves[a] [i]){ //returns true if a legal move is confirmed.
            legalStatus = true; 
        }
        return legalStatus;
    }
    
    /**
     * Integer Arraylist created for returning all legal tiger eats for a tiger in position A. 
     */
    public ArrayList<Integer> legalTigerEats(int a) 
    {
        ArrayList<Integer> legalTigerArr = new ArrayList<Integer>(); //int arrayList to hold values for possible tiger eats in specified location. 
        for (int i = 0; i < legalEats[a].length; i++) { //retrieve each value as long as the list isnt empty. Uses length to ensure no infinity.
            int x = legalEats[a][i];    //gets the int at specified location
            legalTigerArr.add(x);       //adds to the array
        }
        return legalTigerArr;           //returns a complete ArrayList
    }
    
    /**
     * Returns true if a tiger in int A can eat a goat in B. 
     * This along with legalTigerEats (above) were used in conjunction as an alternative for TODO23
     */
    public boolean isLegalEat(int a, int b)
    {  
        int i = 0; //instance variable for loop to run through array
        boolean legalStatus = false; //default value
        while (b != legalMoves[a] [i] && i < legalMoves[a].length) {//a = goatLoc, b = goatDestination. 
            i += 1; //increments i by one to keep going through the 2d array until a match is found
        } 
        if (b == legalMoves[a] [i]){
            legalStatus = true;     //Upon finding a match, return true
        }
        return legalStatus;         //no match found
    }
    
    /**
     * This method was not used. Instead, isLegalEat, legalTigerEats<>, and GameViewer.TigersMove() took its place. 
     */
    public boolean canEatGoat(int tigerLoc, Board bd, int[] scapeGoat)
    {
        //TODO 23  
        return false;        
     }
}
