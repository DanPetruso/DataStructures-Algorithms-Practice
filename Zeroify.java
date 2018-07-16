import java.util.HashSet;

//Question 1.7: Cracking the Coding Interview
//Write an algorithm such that if an element in an MxN matrix is 0,
//its entire row and column are set to 0.

public class Zeroify {
    public static void main(String[] args){
        int[][] m = {{1,1,0,1,1},{0,1,1,1,1},{1,1,1,1,1},{1,1,1,0,1}};
        printMatrix(m);
        zeroify(m);
        printMatrix(m);
    }
    public static void zeroify(int[][] m){
        HashSet<Integer> row = new HashSet<>();
        HashSet<Integer> col = new HashSet<>();

        for (int r = 0; r < m.length; r++){
            for (int c = 0; c < m[0].length; c++) {
                if(m[r][c]==0){
                    row.add(r);
                    col.add(c);
                }
            }
        }

        for (int r = 0; r < m.length; r++){
            for (int c = 0; c < m[0].length; c++) {
                if(row.contains(r) || col.contains(c)){
                    m[r][c] = 0;
                }
            }
        }
    }

    public static void printMatrix(int[][] m){
        for(int r = 0; r < m.length; r++){
            System.out.println();
            for(int c = 0; c < m[0].length; c++){
                System.out.print(m[r][c] + " ");
            }
        }
        System.out.println();
    }
}
