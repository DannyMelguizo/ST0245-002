/**
 * La clase Fecha tiene la intención de representar el tipo abstracto fecha.
 * Aunque ya existen librerías encargadas de esta funcion:
 * @see <a href="http://www.baeldung.com/java-8-date-time-intro"> Ver documentacion tipo Time </a>
 * En este ejercicio podemos tener una compresión más profunda de su funcionamiento interno.
 * 
 * @author Mauricio Toro, Andres Paez
 * @version 1
 */

public class Fecha {

    /*
    varibales con atributo final indican que una variable es de tipo 
    constante, es decir, no admitirá cambios después de su declaración y asignación de valor.
    final determina que un atributo no puede ser sobreescrito o redefinido.
    Se le asigna esta característica para evitar que se sobrescriban valores.

    tener en cuenta tipado de las 3 variables!.
     */

    private final short anyo;
    private final byte mes;
    private final byte dia;

    /**
     * Se inicializan las variables globales en el constructor de manera que no posean valores nulos o 0s.
     */
    public Fecha(short a, byte m, byte d) {
        this.dia = d;
        this.mes = m;
        this.anyo = a;
    }

    /**
     * Método para obtener la variable global dia.
     *
     * @return el dia
     */
    public int dia() {
        return dia;
    }

    /**
     * Método para obtener la variable global mes.
     *
     * @return el mes
     */
    public int mes() {
        return mes;
    }

    /**
     * Método para obtener la variable global anyo.
     *
     * @return el año
     */
    public int anyo() {
        return anyo;
    }

    /**
     * @param otra representa la fecha con la cual se va a comparar.
     *
     * El método comparar se encarga de devolvernos respuesta a tres posibilidades.
     * 1: si la fecha es menor que la otra retorna -1.
     * 2: si la fecha es igual que la otra retorna 0.
     * 3: si la fecha es mayor que la otra retorna 1.
     *
     * @return -1 sí es menor; 0 sí es igual; 1 sí es mayor.
     *
     */

    public int comparar(Fecha otra) {
        if(anyo() < otra.anyo()){
            return -1;   
        }
        if(anyo() > otra.anyo()){
            return 1;   
        }
        if(mes() < otra.mes()){
            return -1;   
        }
        if(mes > otra.mes()){
            return 1;
        }
        if(dia() < otra.dia()){
            return -1;   
        }
        if(dia() > otra.dia()){
            return 1;   
        }
        return 0;
    }

    /**
     * toString se encargará de convertir el tipo abstracto fecha en un tipo cadena
     * para su posterior visualización
     *
     * @return una cadena que contiene la fecha
     */
    public String toString() {
        return this.dia + "/" + this.mes + "/" + this.anyo;
    }
}
