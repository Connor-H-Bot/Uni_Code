/**
 * Maintains and updates the status of the board
 * i.e. the locations of goats and tigers
 *
 * @Student 1 Name: Connor Harris
 * @Student 1 Number: 23208009
 * 
 * @Student 2 Name: Kai Stewart-Wynne
 * @Student 2 Number: 23095602
 */
public class Board
{
    // An enumated type for the three possibilities
    private enum Piece {GOAT, TIGER, VACANT};
    Piece[] board;
    /**
     * Constructor for objects of class Board.
     * Initializes the board VACANT.
     */
    public Board()
    {
        board = new Piece[24];       //creates board with 24 locations
        for (int i=0; i<board.length; i++){ 
            board[i] = Piece.VACANT; // sets each location to VACANT
        }
    }
            
    /**
     * Checks if the location a is VACANT on the board
     */
    public boolean isVacant(int a)
    {
        if (a < 0) {
            return false;
        }
        if (board[a] == Piece.VACANT){ 
            return true;
        }
            else {    
            return false;
        }
    }

    /**
     * Sets the location a on the board to VACANT
     */
    public void setVacant(int a)
    {
        board[a] = Piece.VACANT;
    }
    
    /**
     * Checks if the location a on the board is a GOAT
     */
    public boolean isGoat(int a)
    {
        if (a < 0) {
            return false;
        }
        if (board[a] == Piece.GOAT){
            return true;
        }
        else{
            return false;
        }
    }

    /**
     * Sets the location a on the board to GOAT
     */
    public void setGoat(int a)
    {
        board[a] = Piece.GOAT;
    }
    
    /**
     * Checks if the location a on the board is a TIGER
     */
    public boolean isTiger(int a)
    {
        if (board[a] == Piece.TIGER){
            return true;
        }
            else{
            return false;
        }   
    }
    
    /**
     * Sets the location a on the board to TIGER
     */
    public void setTiger(int a)
    {
        board[a] = Piece.TIGER;
    }
    
    /**
     * Moves a piece by swaping the contents of a and b
     */
    public void swap(int a, int b)
    {
        Piece x = board[a]; //instance variable x to help swapping
        board[a] = board[b];
        board[b] = x;
    }
}