import java.util.ArrayList;

public class Combinations {
    private ArrayList<String> combinations = new ArrayList<>();
    private String s;
    private int index; //keeps track of what letter in the string we are on

    public Combinations(String s){
        this.s = s;
        index = s.length()-1; // starts at the end, work our way down
    }

    public void getAllCombinations(){
        if(index < 0) return;

        //we get the current character our index and add it to our arraylist
        String currChar = s.charAt(index) + "";
        combinations.add(currChar);

        //we then add our current character to all other previous combinations
        int i = 0;
        while(!currChar.equals(combinations.get(i))){
            combinations.add(currChar + combinations.get(i));
            i++;
        }

        //decrement index to get the next letter in our string and recall the function
        index--;
        getAllCombinations();
    }

    public void printCombos(){
        for(String x : combinations){
            System.out.println(x);
        }
    }
}
