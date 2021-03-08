import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for(int i=0;i<num;i++) {
			for(int j=0;j<num;j++) {
				if(j<i) System.out.print(" ");
				else System.out.print("*");
			}
			System.out.println();
		}
	}
}