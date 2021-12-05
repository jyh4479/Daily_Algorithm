import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void printAns(boolean[] visited, ArrayList<Integer> dataList) {
		ArrayList<Integer> ans = new ArrayList<Integer>();

		for (int i = 0; i < visited.length; i++) {
			if (visited[i]) ans.add(dataList.get(i));
		}

		Collections.sort(ans);

		for (Integer an : ans) System.out.println(an);

		System.exit(0);
	}

	public static void printList(boolean[] visited, ArrayList<Integer> dataList) {
		int sum = 0;

		for (int i = 0; i < visited.length; i++) {
			if (visited[i]) sum += dataList.get(i);
		}

		if (sum == 100) printAns(visited, dataList);
	}


	public static void selNumber(boolean[] visited, ArrayList<Integer> dataList, Integer cnt) {
		if (cnt == 7) {
			printList(visited, dataList);
		} else {
			for (int i = cnt; i < visited.length; i++) {
				if (!visited[i]) {
					visited[i] = true;
					selNumber(visited, dataList, cnt + 1);
					visited[i] = false;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ArrayList<Integer> dataList = new ArrayList<Integer>();
		boolean[] visited = new boolean[9];

		for (int i = 0; i < 9; i++) {
			Integer inputData = sc.nextInt();
			dataList.add(inputData);
			visited[i] = false;
		}


		selNumber(visited, dataList, 0);

//        for (int i = 0; i < 9; i++) {
//            System.out.println(dataList.get(i) + " " + visited[i]);
//        }
	}
}
