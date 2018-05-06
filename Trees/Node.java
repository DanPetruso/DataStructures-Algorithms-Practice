//nodes for constructing a binary tree

public class Node {

    private Node left;
    private Node right;
    private int val;

    public Node(Node left, Node right, int val){
        this.left = left;
        this.right = right;
        this.val = val;
    }

    public Node getLeft(){ return left;}
    public Node getRight(){ return right;}
    public int getVal(){ return val;}

}
