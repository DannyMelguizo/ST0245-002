import java.util.*;
import java.io.*;

public class ArchivoCSV
{
    public static void main(String[] args){
          BufferedReader br = null;
          ArrayList<String> listaDatos = new ArrayList();
          try {
             Scanner myObj = new Scanner(System.in);
             System.out.println("Ingrese el nombre de la carpeta");
             String nombreCarpeta = myObj.nextLine();
             System.out.println("Ingrese el nombre del archivo sin la extension");
             String nombreArchivo = myObj.nextLine();
             br = new BufferedReader(new FileReader("./archivos_csv/" + nombreCarpeta + "/" + nombreArchivo + ".csv"));
             String line = br.readLine();
             while (null!=line) {
                String datos = line;
                System.out.println(datos);
                listaDatos.add(datos);
                line = br.readLine();
             }
             
          } catch (Exception e) {
             System.out.println(e);
          }
    }
    
}
