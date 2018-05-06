/*The height of a tree is defined to be the max distance from root node to and leaf node.
Write a function that calculates height height of any binary tree
Test tree looks like:
        a
      /   \
     b     c
          /  \
         d    e
             /
            f
           / \
          g   h
 */

public class HeightOfTree {
    public static int getHeight(Node node){

        if(node.getLeft() != null && node.getRight() != null){
            return Math.max(getHeight(node.getLeft()), getHeight(node.getRight())) + 1;
        }
        else if(node.getRight() != null){
            return getHeight(node.getRight()) + 1;
        }
        else if(node.getLeft() != null){
            return  getHeight((node.getLeft())) + 1;
        }
        return 0;
    }
    public static void main(String[] args){
        Node h = new Node(null, null, 7);
        Node g = new Node(null, null, 6);
        Node f = new Node(g, h, 5);
        Node e = new Node(f, null, 4);
        Node d = new Node(null, null, 3);
        Node c = new Node(d, e, 2);
        Node b = new Node(null, null, 1);
        Node a = new Node(b, c, 0);

        System.out.println(getHeight(a));
    }
}
