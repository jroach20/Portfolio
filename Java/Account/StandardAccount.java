public abstract class StandardAccount {

     //Attributes associated with package costs.
     protected double fixedPackageCost;
     protected double daytimePhoneMinuteCost;
     protected double nighttimePhoneMinuteCost;
     protected double broadbandCostPerMegabyte;
     protected int includedBroadband;

     //Other attributes associated with a type of user account.
     protected int numberOfChannels;
     protected boolean spotifyProvided;
     protected boolean musicProvided;

     //Attributes associated with usage amounts by the customer.
     private int daytimeMinutes;
     private int nighttimeMinutes;
     private int broadbandUsage;

     public StandardAccount (int daytimeMinutes, int nighttimeMinutes, int broadbandUsage)  {
        this.daytimeMinutes = daytimeMinutes;
        this.nighttimeMinutes = nighttimeMinutes;
        this.broadbandUsage = broadbandUsage;
     }

     //Accessors
     public double getFixedPackageCost ()  {
        return fixedPackageCost;
     }

     public double getDaytimePhoneMinuteCost ()  {
        return daytimePhoneMinuteCost;
     }

     public double getNighttimePhoneMinuteCost ()  {
        return nighttimePhoneMinuteCost;
     }

     public double getBroadbandCostPerMegabyte ()  {
        return broadbandCostPerMegabyte;
     }

     public int getIncludedBroadband()  {
        return includedBroadband;
     }

     public int getNumberOfChannels ()  {
        return numberOfChannels;
     }

     public int getDaytimeMinutes ()  {
        return daytimeMinutes;
     }

     public int getNighttimeMinutes ()  {
        return nighttimeMinutes;
     }

     public int getBroadbandUsage ()  {
        return broadbandUsage;
     }

     public boolean isSpotifyProvided ()  {
        return spotifyProvided;
     }

     public boolean isMusicProvided ()  {
        return musicProvided;
     }

     // A method to be defined in the subclasses.
     public abstract String accountType ();

     //***  Costs
     public double daytimePhoneCost ()  {
        return ( getDaytimeMinutes() * getDaytimePhoneMinuteCost() );
     }

     public double nighttimePhoneCost ()  {
        return ( getNighttimeMinutes() * getNighttimePhoneMinuteCost() );
     }

     public double broadbandCost ()  {
        int extraBroadband = Math.max(0, getBroadbandUsage() - getIncludedBroadband() );
        return ( extraBroadband * getBroadbandCostPerMegabyte() );
     }

     public double totalCost ()  {
        return ( getFixedPackageCost() + daytimePhoneCost() + nighttimePhoneCost() + broadbandCost() );
     }

     //Print a summary of information about the account.
     public void printAccountSummary ()  {
        System.out.println("Account Summary for " + accountType() );
        System.out.printf("Package Cost: %.2f\n", getFixedPackageCost() );
        System.out.printf("Cost of daytime calls: %.2f/min\n", getDaytimePhoneMinuteCost() );
        System.out.printf("Cost of evening and weekend calls: %.2f/min\n", getNighttimePhoneMinuteCost() );
        System.out.println("Number of Channels: " + getNumberOfChannels() );
        System.out.println("Broadband Included: " + getIncludedBroadband() +"Mb");
        System.out.println("Broadband Cost (above included limit): " + getBroadbandCostPerMegabyte() +"/Mb");
        System.out.printf("Total daytime calls cost: %.2f\n", daytimePhoneCost() );
        System.out.printf("Total evening calls cost: %.2f\n", nighttimePhoneCost() );
        System.out.printf("Total (extra) broadband cost: %.2f\n", broadbandCost() );
        System.out.printf("Total cost: %.2f\n", totalCost() );
        if ( isSpotifyProvided() )
            System.out.println("Spotify Account provided");
        if ( isMusicProvided() )
            System.out.println("Music on Demand provided");
     }

}
