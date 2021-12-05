import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static int ans = 0;
	public static int S = 0;

	public static void selNumber(boolean[] visited, Integer[] dataList, int cnt, int sel, int cur) {
		if (cnt == sel) {

//            System.out.println(Arrays.toString(visited));

			int sum = 0;
			for (int i = 0; i < visited.length; i++) {
				if (visited[i]) sum += dataList[i];
			}

			if (S == sum) {
				ans += 1;
			}
		} else {
			for (int i = cur; i < visited.length; i++) {
				if (!visited[i]) {
					visited[i] = true;
					selNumber(visited, dataList, cnt, sel + 1, i + 1);
					visited[i] = false;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		S = sc.nextInt();

		Integer[] dataList = new Integer[N];
		boolean[] visited = new boolean[N];

		for (int i = 0; i < N; i++) {
			int data = sc.nextInt();
			dataList[i] = data;
			visited[i] = false;
		}

		for (int i = 1; i <= N; i++) {
			selNumber(visited, dataList, i, 0, 0);
		}
		System.out.println(ans);
	}
}
