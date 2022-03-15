import java.awt.*;
import java.awt.event.*; 
import javax.swing.SwingUtilities;
import java.util.ArrayList;
    /**
    * Controls the drawing of the board and game play. 
    * Allows the human player to make goat moves.
    * Calls AIplayer to make tiger moves.
    *
    * @Student 1 Name: Connor Harris
    * @Student 1 Number: 23208009
    * 
    * @Student 2 Name: Kai Stewart-Wynne
    * @Student 2 Number: 23095602
    */

    
    
public class GameViewer implements MouseListener
{
    // instance variables
    private int bkSize; // block size - all other measurements to be derived from bkSize
    private int brdSize; // board size
    private SimpleCanvas sc; // an object of SimpleCanvas to draw 
    private GameRules rules; // an object of GameRules
    private Board bd; // an object of Board
    private AIplayer ai; //an object of AIplayer
    private int pieceToBeMoved;
    private int pieceToMoveTo;
    
    // 2D coordinates of valid locations on the board in steps of block size                                  
    public static final int[][] locs = {{1,1},                  {4,1},                  {7,1},
    
                                                {2,2},          {4,2},          {6,2},
                                                
                                                        {3,3},  {4,3},  {5,3}, 
                                                        
                                        {1,4},  {2,4},  {3,4},          {5,4},  {6,4},  {7,4},
                                        
                                                        {3,5},  {4,5},  {5,5},
                                                        
                                                {2,6},          {4,6},          {6,6},        
                                        
                                        {1,7},                  {4,7},                  {7,7} };
                                 
    // source and destination for the goat moves                             
    private int[] mov = {-1,-1}; //-1  means no selection
    /**
     * Constructor for objects of class GameViewer
     * Initializes instance variables and adds mouse listener.
     * Draws the board.
     */
    
    public GameViewer(int bkSize)
    {        
        this.bkSize = bkSize;
        brdSize = bkSize*8;
        sc = new SimpleCanvas("Tigers and Goats", brdSize, brdSize, Color.BLUE);
        sc.addMouseListener(this);           
        rules = new GameRules();
        bd = new Board();
        ai = new AIplayer();              
        drawBoard(); 
        pieceToBeMoved = -1;
        pieceToMoveTo = -1;
    }
    
    /**
     * Constructor with default block size
     */
    public GameViewer( )
    {
        this(80); 
    }
    
    /**
     * Draws the board lines and the pieces as per their locations.
     * Drawing of lines is provided, students to implement drawing 
     * of pieces and number of goats.
     */
    private void drawBoard()
    {
        sc.drawRectangle(0,0,brdSize,brdSize,Color.BLUE); //wipe the canvas               
        // Draw the lines
        for(int i=1; i<9; i++)
        {
            //draw the red lines
            if(i<4)
                sc.drawLine(locs[i-1][0]*bkSize, locs[i-1][1]*bkSize,
                        locs[i+5][0]*bkSize, locs[i+5][1]*bkSize, Color.red);
            else if(i==4)
                sc.drawLine(locs[i+5][0]*bkSize, locs[i+5][1]*bkSize,
                        locs[i+7][0]*bkSize, locs[i+7][1]*bkSize, Color.red);
            else if(i==5)
                sc.drawLine(locs[i+7][0]*bkSize, locs[i+7][1]*bkSize,
                        locs[i+9][0]*bkSize, locs[i+9][1]*bkSize, Color.red);              
            else
                sc.drawLine(locs[i+9][0]*bkSize, locs[i+9][1]*bkSize,
                        locs[i+15][0]*bkSize, locs[i+15][1]*bkSize, Color.red);              
           
            if(i==4 || i==8) continue; //no more to draw at i=4,8
            // vertical white lines
            sc.drawLine(i*bkSize, i*bkSize,
                        i*bkSize, brdSize-i*bkSize,Color.white);            
            // horizontal white lines
            sc.drawLine(i*bkSize,         i*bkSize,
                        brdSize-i*bkSize, i*bkSize, Color.white);  
        }
        // Draw the goats and tigers
        // Display the number of goats        
        for (int i=0; i<locs.length; i++){
            if (bd.isGoat(i) == true){              //make a circle for the goats
                sc.drawDisc(locs[i][0] * bkSize, locs[i][1] * bkSize,
                bkSize/3, // goat disc size
                Color.black);
                //above code draws the black circle to serve as background to the green
                sc.drawDisc(locs[i][0] * bkSize, locs[i][1] * bkSize,
                bkSize/4, // goat disc size
                Color.green); // colour of goat is green
                sc.drawString("Number of goats: " + Integer.toString(rules.getNumGoats()), 20, 20, Color.white); //display count
            }
                                                    //make a square for the tigers
            else if (bd.isVacant(i) == false){
                sc.drawRectangle(locs[i][0] * bkSize - (bkSize/3), //x1
                locs[i][1]*bkSize - (bkSize/3), //y1
                locs[i][0]*bkSize + (bkSize/3), // x2
                locs[i][1]*bkSize + (bkSize/3), //y2
                Color.black); 
                //above code draws black background
                sc.drawRectangle(locs[i][0] * bkSize - (bkSize/4), //x1
                locs[i][1]*bkSize - (bkSize/4), //y1
                locs[i][0]*bkSize + (bkSize/4), // x2
                locs[i][1]*bkSize + (bkSize/4), //y2
                Color.red); //colour of tiger is red
                sc.drawString("Number of tigers: " + Integer.toString(rules.getNumTigers()), 200, 20, Color.white); //display count
            }
        }
    }
    
    /**
     * If vacant, place a goat at the user clicked location on board.
     * Update goat count in rules and draw the updated board
    */
    public void placeGoat(int loc) 
    {   
        if ((bd.isVacant(loc)) && (rules.getNumGoats() < 12)){ //Executes this loop if still in phase 1
            rules.addGoat(1);                                  // adds 1 to the goat count
            bd.setGoat(loc);                                   //sets a loc from vacant to oppucpied by goat
            drawBoard();                                       //draw new goat
            if (rules.isGoatsTurn() == false) { //calls upon placeTiger if the 4th, 8,th and 12th tigers are placed (code in rules.AddGoat();)
                this.placeTiger();
            }
        } 
        if (rules.isMoveStage() == false && (rules.isGoatsTurn() == false)) { //idk this looks wrong
            rules.addGoat(1); 
        }
    } 
    
    /**
     * Calls the placeTiger method of AIplayer to place a tiger on the board.
     * Increments tiger count in rules.
     * Draws the updated board.
     */
    public void placeTiger() 
    {   
        //During phase 1, if the conditions are met the computer will place a tiger at a random location. 
        if ((rules.isGoatsTurn() == false) && (rules.isMoveStage() == false) && (ai.getnTigers() != 3)){
            rules.incrTigers();
            ai.placeTiger(bd);
            drawBoard();
        } 
        if (rules.getNumTigers() == 3 && rules.getNumGoats() == 12 && (rules.isMoveStage() == false))  { //Change to phase 2 after final tiger is places.
            rules.changeMoveStage();
        }
    }
    
    /**
     * Toggles goat selection - changes the colour of selected goat.
     * Resets selection and changes the colour back when the same goat is clicked again.
     * Selects destination (if vacant) to move and calls moveGoat to make the move.
     */
    public void selectGoatMove(int loc) 
    {    
        //If the user clicks on a goat change its color and return so that a destination can be added. 
        if ((bd.isGoat(loc) == true) && (rules.isGoatsTurn() == true) && (pieceToBeMoved == -1) && (pieceToMoveTo == -1)) {
            pieceToBeMoved = loc;
            sc.drawDisc(locs[pieceToBeMoved][0] * bkSize, locs[pieceToBeMoved][1] * bkSize,
            bkSize/4, // goat disc size 
            Color.yellow);
            return;
        } 
        //Once a goat to move has been selected, if the user selects the same goat this is executed. 
        if ((bd.isTiger(loc) == false) && (rules.isGoatsTurn() == true) && (pieceToBeMoved == loc)) { 
            pieceToMoveTo = loc;  
        } 
        //if the same goat is clicked on, remove the colour and throw away selection.
        if ((pieceToMoveTo == pieceToBeMoved) && (pieceToMoveTo != -1)) { 
            sc.drawDisc(locs[pieceToBeMoved][0] * bkSize, locs[pieceToBeMoved][1] * bkSize,
            bkSize/4, 
            Color.green);
            pieceToBeMoved = -1;
            pieceToMoveTo = -1;
            return;
        }
        //if the goat destination is illegal the selection is thrown away and the method is ended.
        if ((rules.isLegalMove(pieceToBeMoved, pieceToMoveTo) == false) && (pieceToMoveTo != -1) || (rules.isLegalMove(pieceToBeMoved, loc) == false)){
            drawBoard();
            pieceToBeMoved = -1;
            pieceToMoveTo = -1;
            return;
        }
        //Once there is a vacant destination, valid location, and the move is legal move the goat to the position. 
        if ((bd.isVacant(loc) == true) && (rules.isGoatsTurn() == true) && (pieceToBeMoved != -1) 
            && (rules.isLegalMove(pieceToBeMoved, loc) == true)) { 
            pieceToMoveTo = loc;
            moveGoat();
        }
    }    
    
     /**
     * Make the selected goat move if: move is legal, piece is vacant, and its the goats turn to move. 
     * If did make a goat move, then update board, draw the updated board, reset mov to -1,-1.
     * and call tigersMove() since after every goat move, there is a tiger move.
     */
    public void moveGoat() 
    {          
        if ((rules.isLegalMove(pieceToBeMoved, pieceToMoveTo) == true) && (bd.isVacant(pieceToMoveTo) == true) && (rules.isGoatsTurn() == true)) {
            bd.swap(pieceToBeMoved, pieceToMoveTo);
            drawBoard();
            rules.changeTurn();
            tigersMove();
            pieceToBeMoved = -1;
            pieceToMoveTo = -1;
        } 
    } 
  
    /**
     * The brain for the tiger - this is the tigers move deciding mathod. 
     * If Tigers cannot move, display "Goats Win!".
     * If goats are less than 6, display "Tigers Win!".
     * No need to terminate the game.
     */
    public void tigersMove()
    {    
    int x = 0;
    for (x = 0; x < 24; x++) { //initial loop to find a tiger. This loop is used to find an opppurtunity to eat. If no option leads to eat, move onto move
        int z = 0;
        int potentialMoveDestination = 0; //place where tiger can land after kill
        int potentialEatLocation = 0;     //place where goat to be killed is
        if (bd.isTiger(x) == true) {      //once tiger is found
            ArrayList<Integer> legalTigerEatsArr = rules.legalTigerEats(x); //import legalmoves from rules as arrayList since the size is variable
            if (legalTigerEatsArr.size() > 0) {                             //check the list isnt empty (ie the tiger at [4] has no eat options)
                for (z = 0; z < legalTigerEatsArr.size(); z += 2) {         //continue the loop only while there is valid spaces
                    potentialEatLocation = legalTigerEatsArr.get(z);        //potential goat to be eaten
                    potentialMoveDestination = legalTigerEatsArr.get(z + 1);//potential location
                    if ((bd.isGoat(potentialEatLocation) == true) && (bd.isVacant(potentialMoveDestination) == true)) { //executes if a kill can be made
                       rules.addGoat(-1);
                       bd.swap(x, potentialMoveDestination);
                       bd.setVacant(potentialEatLocation);
                       rules.changeTurn();
                       drawBoard();
                       if (rules.getNumGoats() < 6) {
                           sc.drawString("Tigers win!! All hail the AI overlord", 50, 80, Color.white);
                       }
                       return; 
                    }
                }
            }
        }
    }
    int a = 0; //another int for looping
    for (x = 0; x < 24; x++) {                          //select tiger to move spaces since a kill cannot be found
        if (bd.isTiger(x) == true) {                    //find a tiger
            for (a = 0; a < 24; a++) {                  //iterate through positions for tiger to move to
                if (rules.isLegalMove(x, a) == true) {  //once found a legal position
                    if (bd.isVacant(a) == true) {       // check if its vacant
                    bd.swap(x, a);      //swap positions
                    rules.changeTurn(); //change turn
                    drawBoard();        //draw the new board
                    return;             //exit the method
                    }
                }
            }
        }
    }
        //since no moves can be made by the tigers, goats win.
        sc.drawString("GOATS WIN!!! Humans > Machines....for now", 50, 80, Color.white);
    }
        
    /**
     * Respond to a mouse click on the board. 
     * Get a valid location nearest to the click (from GameRules). 
     * If nearest location is still far, do nothing. 
     * Otherwise, call placeGoat to place a goat at the location.
     * Call this.placeTiger when it is the tigers turn to place.
     * When the game changes to move stage, call selectGoatMove to move 
     * the user selected goat to the user selected destination.
     */
    public void mousePressed(MouseEvent e) 
    {
        int loc = rules.nearestLoc(e.getX(), e.getY(), bkSize);
           if (rules.isMoveStage() == false) { // checks if its not in the moving stage
               if (rules.isGoatsTurn() == true) { // checks if its goats turn
                   if ( loc != -1){ // checks if its valid location
                   placeGoat(loc); //places a goat on the valid location
                }
            }
            else { //tigers turn place a tiger and increment
                this.placeTiger(); 
            }
        }
            else { 
                // if in the moving stage select a goat and move to a location
                selectGoatMove(loc);
            }
    }
        
    public void mouseClicked(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
}
