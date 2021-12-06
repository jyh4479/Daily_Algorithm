import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int E = sc.nextInt();
		int S = sc.nextInt();
		int M = sc.nextInt();


		int checkE = 1;
		int checkS = 1;
		int checkM = 1;
		int ans = 1;

		while (true) {
			if (E == checkE && S == checkS && M == checkM) {
				System.out.println(ans);
				break;
			}
			checkE++;
			checkS++;
			checkM++;

			if (checkE > 15) checkE = 1;
			if (checkS > 28) checkS = 1;
			if (checkM > 19) checkM = 1;

			ans++;
		}
	}
}