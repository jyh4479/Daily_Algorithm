import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		for(int a=num;a>0;a--) {
			for(int i=0;i<a;i++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}