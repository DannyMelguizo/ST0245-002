import java.util.*;
import java.lang.Math.*;
public class Laboratorio1 {

    public static int LongitudSubSecComun(String string1, String string2){

        return LongitudSubSecComunAux(string1,string2,string1.length(),string2.length());
    }

    private static int LongitudSubSecComunAux(String string1, String string2, int m, int n) {
        if(m == 0 || n == 0){
            return 0;
        }
        if(string1.charAt(m-1)==string2.charAt(n-1)){
            return 1 + LongitudSubSecComunAux(string1, string2, m-1, n-1);
        }
        return Math.max(LongitudSubSecComunAux(string1, string2, m-1, n-1), LongitudSubSecComunAux(string1, string2, m-1,n-1));
    }

    public static int ways(int n){
        if(n <= 3){ 
            return n;
        }
        return ways(n-1) + ways(n-2);
    }

    /**
     * 
    public static void main(String [] args){
    Scanner scan = new Scanner(System.in);
    System.out.println("ingrese String1");
    String string1 = scan.next();
    System.out.println("ingrese String2");
    String string2 = scan.next();
    System.out.println(LongitudSubSecComun(string1, string2));
    }*/

}