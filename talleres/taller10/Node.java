public class Node {

    public Node left,rigth;
    public int data;

    public Node(int data) {
        this.left = null;
        this.rigth = null;
        this.data = data;
    }

    public int getData(){
        return this.data;
    }

    public void setData(int data){
        this.data = data;
    }

    public Node getLeftNode(){
        return this.left;  
    }

    public Node getRigthNode(){
        return this.rigth;  
    }

    public void setLeftNode(Node left){
        this.left = left;

    }

    public void setRigthNode(Node rigth){
        this.rigth = rigth;

    }
}
