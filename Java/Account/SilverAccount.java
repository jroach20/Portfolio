public class SilverAccount extends StandardAccount implements AccountConstants {

     public SilverAccount (int daytimeMinutes, int nighttimeMinutes, int broadbandUsage)  {
        //Call the constructor of the parent class.
        super(daytimeMinutes, nighttimeMinutes, broadbandUsage);

        //Set the package costs and other attributes here.
        fixedPackageCost = SILVER_FIXED_COSTS;
        daytimePhoneMinuteCost = SILVER_DAYTIME_MINUTE_CHARGE;
        nighttimePhoneMinuteCost = SILVER_NIGHTTIME_MINUTE_CHARGE;
        broadbandCostPerMegabyte = SILVER_MEGABYTE_CHARGE;
        includedBroadband = SILVER_INCLUDED_BROADBAND;
        numberOfChannels = SILVER_NUMBER_OF_CHANNELS;
        spotifyProvided = SILVER_SPOTIFY_PROVIDED;
        musicProvided = SILVER_MUSIC_PROVIDED;
     }

     public String accountType()  {
        return "Silver Account";
     }

}
