public class GoldAccount extends StandardAccount implements AccountConstants {

     public GoldAccount (int daytimeMinutes, int nighttimeMinutes, int broadbandUsage)  {
        //Call the constructor of the parent class.
        super(daytimeMinutes, nighttimeMinutes, broadbandUsage);

        //Set the package costs and other attributes here.
        fixedPackageCost = GOLD_FIXED_COSTS;
        daytimePhoneMinuteCost = GOLD_DAYTIME_MINUTE_CHARGE;
        nighttimePhoneMinuteCost = GOLD_NIGHTTIME_MINUTE_CHARGE;
        broadbandCostPerMegabyte = GOLD_MEGABYTE_CHARGE;
        includedBroadband = GOLD_INCLUDED_BROADBAND;
        numberOfChannels = GOLD_NUMBER_OF_CHANNELS;
        spotifyProvided = GOLD_SPOTIFY_PROVIDED;
        musicProvided = GOLD_MUSIC_PROVIDED;
     }

     public String accountType()  {
        return "Gold Account";
     }

}
