public class Area {
	 public void areaofCircle (Decimal x){
        Decimal Area=3.14*x*x;
        system.debug('Area of circle is'+Area);
    }
public void areaofRectangle (Decimal x,Decimal y){
        Decimal Area=x*y;
        system.debug('Area of Rectangle is'+Area);
    }
    public void areaofTriangle (Decimal x,Decimal y){
        Decimal Area=0.5*x*y;
        system.debug('Area of Triangle is'+Area);
    }
}