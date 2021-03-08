import java.util.*;

public class main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int M=sc.nextInt();
		
		int map[][] = new int[N][M];
		boolean visit[][] = new boolean[N][M];
		
		for(int i=0;i<N;i++) {
			String temp = sc.next();
			for(int j=0;j<M;j++) {
				map[i][j] = temp.charAt(j) - 48;
			}
		}
		
		// BFS 시작 //
		int dictx[]= {0,0,1,-1};
		int dicty[]= {1,-1,0,0};
		
		Queue<Integer> qx=new LinkedList<>();
		Queue<Integer> qy=new LinkedList<>();
		
		qx.add(0);
		qy.add(0);
		
		while(!qx.isEmpty() && !qy.isEmpty()) {
			int x = qx.poll();
			int y = qy.poll();
			visit[y][x]=true;
			
			for(int i=0;i<4;i++) {
				int dx=dictx[i]+x;
				int dy=dicty[i]+y;
				
				if(dx<0 || dy<0 || dx>=M || dy>=N) continue;
				
				else {
					if(visit[dy][dx]==false && map[dy][dx]==1) {
						qx.add(dx);
						qy.add(dy);
						visit[dy][dx]=true;
						map[dy][dx]=map[y][x]+1;
					}
				}
			}
		}
		System.out.println(map[N-1][M-1]);
	}
}