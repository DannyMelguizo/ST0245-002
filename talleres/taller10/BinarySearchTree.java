public class BinarySearchTree {
    public static String generarDiagrama(Node nodo){
        String diagram = "";
        if(nodo != null){
            Node left = nodo.getLeftNode();
            Node rigth = nodo.getRigthNode();
            if(left != null){
                diagram += "\t\"" + Integer.toString(nodo.getData()) + "\" -> \"" + Integer.toString(nodo.getLeftNode().getData()) + "\"\n" 
                + generarDiagrama(nodo.getLeftNode()) + generarDiagrama(nodo.getRigthNode());
            } else {
                diagram += "";
            }
            if(rigth != null){
                diagram += ("\t\"" + Integer.toString(nodo.getData()) + "\" -> \"" + Integer.toString(nodo.getRigthNode().getData()) + "\"\n"
                    + generarDiagrama(nodo.getLeftNode()) + generarDiagrama(nodo.getRigthNode()));
            } else {
                diagram += "";
            }
        }
        return diagram;
    }

}