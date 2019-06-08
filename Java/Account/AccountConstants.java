interface AccountConstants {

     //*****  Bronze Account
     //  Bronze Account package costs and other attributes
     static final double BRONZE_FIXED_COSTS = 36.00;
     static final double BRONZE_DAYTIME_MINUTE_CHARGE = 0.12;
     static final double BRONZE_NIGHTTIME_MINUTE_CHARGE = 0.05;
     static final double BRONZE_MEGABYTE_CHARGE = 0.02;

     static final int BRONZE_INCLUDED_BROADBAND = 500;
     static final int BRONZE_NUMBER_OF_CHANNELS = 60;

     static final boolean BRONZE_SPOTIFY_PROVIDED = false;
     static final boolean BRONZE_MUSIC_PROVIDED = false;

     //*****  Silver Account
     //  Silver Account package costs and other attributes
     static final double SILVER_FIXED_COSTS = 46.00;
     static final double SILVER_DAYTIME_MINUTE_CHARGE = 0.12;
     static final double SILVER_NIGHTTIME_MINUTE_CHARGE = 0;
     static final double SILVER_MEGABYTE_CHARGE = 0.01;

     static final int SILVER_INCLUDED_BROADBAND = 1000;
     static final int SILVER_NUMBER_OF_CHANNELS = 130;

     static final boolean SILVER_SPOTIFY_PROVIDED = true;
     static final boolean SILVER_MUSIC_PROVIDED = false;

     //*****  Gold Account
     //  Gold Account package costs and other attributes
     static final double GOLD_FIXED_COSTS = 61.00;
     static final double GOLD_DAYTIME_MINUTE_CHARGE = 0;
     static final double GOLD_NIGHTTIME_MINUTE_CHARGE = 0;
     static final double GOLD_MEGABYTE_CHARGE = 0.01;

     static final int GOLD_INCLUDED_BROADBAND = 1520;
     static final int GOLD_NUMBER_OF_CHANNELS = 230;

     static final boolean GOLD_SPOTIFY_PROVIDED = true;
     static final boolean GOLD_MUSIC_PROVIDED = true;

}
