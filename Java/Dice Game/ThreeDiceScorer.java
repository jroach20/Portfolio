public class ThreeDiceScorer extends ThreeDice{
  int diceScore;
  int sumOfDice;

  public ThreeDiceScorer(int s1, int s2, int s3){
    //gets the dice1,dice2,dice3 attributes from ThreeDice
    super(s1, s2, s3);
    //initialises the sum of the three dice outputs
    sumOfDice= s1+s2+s3;
  }
  //method for calculating the score of the dice (based on what they are classed as)
public int getScore(){
  if (threeSame()== true){

    diceScore = 60;
  }
  if (runOfThree()== true){
    diceScore = 40;
  }
  if (pair()== true){
    diceScore = 20;
  }
  if (allDifferent()== true){
    diceScore = 0;
  }
  diceScore= diceScore+sumOfDice;
  return diceScore;
}
//overrides the getScore as a string so it can be viewed as an integer
public String toString() {
  return(""+getScore());
}
}
