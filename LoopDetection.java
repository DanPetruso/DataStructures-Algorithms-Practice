//Loop Detection
//Given a circular linked list, return the node that starts the loop

public class LoopDetection {
	static Node returnStart(Node head) {
		Node faster = head;
		Node slower = head;
		
		while(faster.next != null && faster != null) {
			slower = slower.next;
			faster = faster.next.next;
			if(faster == slower) break;
		}
		
		if(faster != slower) return null;
		
		slower = head;
		while(faster != slower) {
			faster = faster.next;
			slower = slower.next;
		}
		
		return faster;
		
	}
}

class Node{
	public Node next;
	public char data;
	
	public Node(char data) {
		this.data = data;
	}
}