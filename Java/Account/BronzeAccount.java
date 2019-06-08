public class BronzeAccount extends StandardAccount implements AccountConstants {

     public BronzeAccount (int daytimeMinutes, int nighttimeMinutes, int broadbandUsage)  {
        //Call the constructor of the parent class.
        super(daytimeMinutes, nighttimeMinutes, broadbandUsage);

        //Set the package costs and other attributes here.
        fixedPackageCost = BRONZE_FIXED_COSTS;
        daytimePhoneMinuteCost = BRONZE_DAYTIME_MINUTE_CHARGE;
        nighttimePhoneMinuteCost = BRONZE_NIGHTTIME_MINUTE_CHARGE;
        broadbandCostPerMegabyte = BRONZE_MEGABYTE_CHARGE;
        includedBroadband = BRONZE_INCLUDED_BROADBAND;
        numberOfChannels = BRONZE_NUMBER_OF_CHANNELS;
        spotifyProvided = BRONZE_SPOTIFY_PROVIDED;
        musicProvided = BRONZE_MUSIC_PROVIDED;
     }

     public String accountType()  {
        return "Bronze Account";
     }

}
