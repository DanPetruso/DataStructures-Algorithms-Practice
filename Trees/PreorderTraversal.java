/*Informally, a pre order traversal involves walking around the tree in a counter-clockwise
manner starting at the root, sticking close to the edges, and printing out the nodes as you
encounter them.
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

import java.util.Stack;

public class PreorderTraversal {

    public static void preoderTraversalRecursion(Node node){
        System.out.println(node.getVal());
        if(node.getLeft() != null){
            preoderTraversalRecursion(node.getLeft());
        }
        if(node.getRight() != null){
            preoderTraversalRecursion(node.getRight());
        }
    }

    public static void preoderTraversal(Node head){
        Stack<Node> stck = new Stack();
        stck.push(head);
        while(stck.size() > 0){
            Node curr = stck.pop();
            System.out.println(curr.getVal());
            Node n = curr.getRight();
            if(n!=null) stck.push(n);
            n = curr.getLeft();
            if(n!=null) stck.push(n);
        }
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

       preoderTraversalRecursion(a);
        System.out.println();
       preoderTraversal(a);
    }
}
