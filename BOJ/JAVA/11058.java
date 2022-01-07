import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		ArrayList<Integer> dataList = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			Integer data = sc.nextInt();
			dataList.add(data);
		}

		Collections.sort(dataList);
		ArrayDeque<Integer> q = new ArrayDeque<Integer>(dataList);

		int ans = 0;
		while (q.size() > 2) {
			ans += q.removeLast();
			ans += q.removeLast();
			q.removeLast();
		}
		if (!q.isEmpty()) {
			while (!q.isEmpty()) {
				ans += q.remove();
			}
		}
		System.out.println(ans);
	}
}