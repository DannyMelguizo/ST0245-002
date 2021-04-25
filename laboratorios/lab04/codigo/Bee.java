public class Bee
{
    private double latitude;
    private double longitude;
    private double altitude;

    public Bee (double latitude, double longitude, double altitude){
        this.latitude=latitude;
        this.longitude=longitude;
        this.altitude=altitude;
    }

    public double getLatitude(){
        return latitude;
    }

    public double getLongitude(){
        return longitude;
    }

    public double getAltitude(){
        return altitude;
    }
}
