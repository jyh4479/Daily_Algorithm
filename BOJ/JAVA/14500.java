import java.util.Scanner;

public class Main {

	private static int[] dy = {1, 0, -1, 0};
	private static int[] dx = {0, 1, 0, -1};

	private static int[][] oy = {{-1, 0, 1}, {0, 1, 0}, {1, 0, -1}, {0, -1, 0}};
	private static int[][] ox = {{0, 1, 0}, {1, 0, -1}, {0, -1, 0}, {-1, 0, 1}};

	private static int ans = -1;

	public static void checkOtherCase(int y, int x, int firstSum, int[][] graph) {
		for (int i = 0; i < 4; i++) {
			int sum = firstSum;
			int n=graph.length;
			int m=graph[0].length;
			int ay, by, cy;
			int ax, bx, cx;
			ay = y + oy[i][0];
			by = y + oy[i][1];
			cy = y + oy[i][2];
			ax = x + ox[i][0];
			bx = x + ox[i][1];
			cx = x + ox[i][2];

			if(ay<0 || by<0 || cy<0||ax<0||bx<0||cx<0||
					ay>=n || by>=n || cy>=n || ax>=m || bx>=m || cx>=m){
				continue;
			} else{
				ans=Math.max(ans,firstSum+graph[ay][ax]+graph[by][bx]+graph[cy][cx]);
			}

		}

	}

	public static void dfs(int y, int x, int[][] graph, boolean[][] visit, int cnt, int sum) {
		if (cnt == 4) {
			ans = Math.max(ans, sum);
		} else {
			for (int i = 0; i < 4; i++) {
				int ny = dy[i] + y;
				int nx = dx[i] + x;
				if ((ny >= graph.length) || (nx >= graph[0].length) || (ny < 0) || (nx < 0) || visit[ny][nx]) {
					continue;
				} else {
					visit[ny][nx] = true;
					dfs(ny, nx, graph, visit, cnt + 1, sum + graph[ny][nx]);
					visit[ny][nx] = false;
				}
			}
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int graph[][] = new int[n][m];
		boolean visit[][] = new boolean[n][m];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				graph[i][j] = sc.nextInt();
				visit[i][j] = false;
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				visit[i][j] = true;
				dfs(i, j, graph, visit, 1, graph[i][j]);
				visit[i][j] = false;
				checkOtherCase(i, j, graph[i][j],graph);
			}
		}

		System.out.println(ans);
	}
}