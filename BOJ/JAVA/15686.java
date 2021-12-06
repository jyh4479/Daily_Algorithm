import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static class Location {
		public int y;
		public int x;

		Location(int y, int x) {
			this.y = y;
			this.x = x;
		}
	}

	public static int ans = Integer.MAX_VALUE;

	public static void selChicken(boolean[] visited, ArrayList<Location> houseList, ArrayList<Location> chickenList, int chickenCount, int check, int cnt) {
		if (chickenCount == check) {
			int sum = 0;
			for (int i = 0; i < houseList.size(); i++) {
				int y = houseList.get(i).y;
				int x = houseList.get(i).x;
				int dist = Integer.MAX_VALUE;
				for (int j = 0; j < chickenList.size(); j++) {
					if (!visited[j]) {
						dist = Math.min(dist, Math.abs(y - chickenList.get(j).y) + Math.abs(x - chickenList.get(j).x));
//                        System.out.println(dist);
					}
				}
				sum += dist;
			}
			ans = Math.min(ans, sum);
		} else {
			for (int i = cnt; i < visited.length; i++) {
				if (!visited[i]) {
					visited[i] = true;
					selChicken(visited, houseList, chickenList, chickenCount - 1, check, i);
					visited[i] = false;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[][] maps = new int[N][N];

		ArrayList<Location> houseList = new ArrayList<>();
		ArrayList<Location> chickenList = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int data = sc.nextInt();
				maps[i][j] = data;

				if (data == 1) {
					houseList.add(new Location(i, j));
				} else if (data == 2) {
					chickenList.add(new Location(i, j));
				}
			}
		}

		boolean[] visited = new boolean[chickenList.size()];
		for (int i = 0; i < visited.length; i++) visited[i] = false;
		int chickenCount = chickenList.size();

		selChicken(visited, houseList, chickenList, chickenCount, M, 0);

		System.out.println(ans);
	}
}