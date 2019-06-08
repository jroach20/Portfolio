import java.util.*;

public class AccountUser  {

     public static void main(String[] args)  {

        int daytimePhoneMinutes = inputIntLowerBound(0, "Please enter the number of daytime minutes used per month: ");
        int nighttimePhoneMinutes = inputIntLowerBound(0, "Please enter the number of nighttime minutes used per month: ");;
        int broadbandUsage = inputIntLowerBound(0, "Please enter the number of Megabytes used per month: ");

        StandardAccount bronze = new BronzeAccount(daytimePhoneMinutes, nighttimePhoneMinutes, broadbandUsage);
        StandardAccount silver = new SilverAccount(daytimePhoneMinutes, nighttimePhoneMinutes, broadbandUsage);
        StandardAccount gold = new GoldAccount(daytimePhoneMinutes, nighttimePhoneMinutes, broadbandUsage);

        bronze.printAccountSummary();
        System.out.println();
        silver.printAccountSummary();
        System.out.println();
        gold.printAccountSummary();

        double bronzeCost = bronze.totalCost();
        double silverCost = silver.totalCost();
        double goldCost = gold.totalCost();
        if ( (goldCost <= silverCost) && (goldCost <= bronzeCost) )
             System.out.println("\nGold Account is cheapest cost.");
        else if ( silverCost <= bronzeCost )
             System.out.println("\nSilver Account is cheapest cost.");
        else
             System.out.println("\nBronze Account is cheapest cost.");

        System.out.println();
     }

     public static int inputIntLowerBound (int lowerBound, String s)  {
        Scanner input = new Scanner(System.in);

        int n;
        do {
             System.out.print(s);
             n = input.nextInt();
             if (n < lowerBound)  {
                 System.out.println("Oops, your input was too small!");
             }
        } while (n < lowerBound);

        return n;
     }

}
