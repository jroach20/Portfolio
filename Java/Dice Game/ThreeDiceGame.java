import java.util.Scanner;
import java.util.Random;
public class ThreeDiceGame{

  public static void main( String[] args ) {
  //ATRIBUTES
  int numOfRounds;
  ThreeDiceScorer[] player1;
  ThreeDiceScorer[] player2;
  int p1wins;
  int p2wins;

    //This allows the user to input how many rounds of the game they want to play
    Scanner input = new Scanner(System.in);
    System.out.println("How many rounds of the game do you want to play?(min:1)");
    numOfRounds= input.nextInt();
    //the while loop makes sure that the game will only begin if the user inputs a number higher than 1
    while (numOfRounds<1){
      Scanner tryagain = new Scanner(System.in);
      System.out.println("The number you entered was lower than 1. Let's try a higher number this time: ");
      numOfRounds= tryagain.nextInt();
    }

      //These two variables can now use attributes from the ThreeDiceScorer class
      player1 = new ThreeDiceScorer[numOfRounds];
      player2 = new ThreeDiceScorer[numOfRounds];
      p1wins= 0;
      p2wins= 0;



      //FOR LOOP START
      for (int x=0; x<numOfRounds;x++) {
      //The two variables are swapping the s1,s2,s3 attributes in the ThreeDiceScorers parameters with random numbers generated between 1-6
      player1[x] = new ThreeDiceScorer(1+(int)(6*Math.random()), 1+(int)(6*Math.random()), 1+(int)(6*Math.random()));
      //This is applying the random numbers to the getScore() method that is in ThreeDiceScorer
      player1[x].getScore();

      player2[x] = new ThreeDiceScorer(1+(int)(6*Math.random()), 1+(int)(6*Math.random()), 1+(int)(6*Math.random()));
      player2[x].getScore();

      System.out.println("\nRound "+(x+1));
      //the toString method converts the information in ThreeDiceScorer into a readable format
      System.out.println("Player1 rolls and scores : "+player1[x].toString());
      System.out.println("player2 rolls and scores : "+player2[x].toString());
      //If statements are used to create win conditions.
      if (player1[x].getScore()>player2[x].getScore()){
        System.out.println("PLAYER 1 WINS!");
        p1wins++;
      }

      if (player1[x].getScore()<player2[x].getScore()){
        p2wins++;
        System.out.println("PLAYER 2 WINS!");
      }

      if (player1[x].getScore()==player2[x].getScore()){
        System.out.println("ROUND TIE!");
      }

      if (x==numOfRounds-1){
      System.out.println("\nRounds player 1 won: "+p1wins);
      System.out.println("Rounds player 2 won: "+p2wins);

      if (p1wins>p2wins){
        System.out.println("PLAYER 1 WINS THE GAME!");
      }

      if (p1wins<p2wins){
      System.out.println("PLAYER 2 WINS THE GAME!");
      }
    }

        }
      //END OF FOR LOOP
      }

    }
