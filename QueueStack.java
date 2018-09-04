import java.util.Stack;

//Implement a queue using two stacks

public class QueueStack<T> {
	
	Stack<T> stack1, stack2;
	
	public QueueStack(){
		stack1 = new Stack<T>();
		stack2 = new Stack<T>();
	}
	
	public void add(T value) {
		stack1.push(value);
	}
	
	public void swap() {
		while(!stack1.isEmpty()) {
			stack2.push(stack1.pop());
		}
	}
	
	public void swapBack() {
		while(!stack2.isEmpty()) {
			stack1.push(stack2.pop());
		}
	}
	
	public T peek() {
		swap();
		T item = stack2.peek();
		swapBack();
		
		return item;
	}
	
	public T remove() {
		swap();
		T item = stack2.pop();
		swapBack();
		
		return item;
	}
}