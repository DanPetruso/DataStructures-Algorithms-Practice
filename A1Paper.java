//A1 paper problem from Kattis
//https://open.kattis.com/problems/a1paper
import java.util.*;

public class A1Paper {
	
	public static double getTape(double n) {
		return Math.pow(2, .25) * Math.pow(Math.pow(2, .5) / 2, n);
	}
	
	public static void main(String []args) {
		Scanner input = new Scanner(System.in);
		
		int smallest = input.nextInt();
		
		int neededAmt = 2;
		double totalTape = 0.0;
		
		boolean possible = false;
		
		for(int i = 2; i <= smallest; i++) {
			int currentAmt = input.nextInt();
			totalTape += neededAmt / 2 * getTape(i);
			
			if(currentAmt >= neededAmt) {
				possible = true;
				break;
			}
			neededAmt = (neededAmt - currentAmt) * 2;
		}
		
		System.out.println(possible? totalTape : "impossible");
		
	}
}
