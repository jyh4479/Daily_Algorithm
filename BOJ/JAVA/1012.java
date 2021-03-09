import java.util.*;

public class main {
	public static void dfs(int y, int x, int[][] map,int N, int M) {
		int[] dictx = {0,0,1,-1};
		int[] dicty = {1,-1,0,0};
		
		for(int i=0;i<4;i++) {
			int dx=dictx[i]+x;
			int dy=dicty[i]+y;
			
			if(dx<0 || dy<0 || dx>=M || dy>=N) continue;
			else {
				if (map[dy][dx]==1) {
					map[dy][dx]=0;
					dfs(dy,dx,map,N,M);
				}
			}
		}
	}
	
	public static void Main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num=sc.nextInt();
		
		for(int repeat=0;repeat<num;repeat++) {
			int M,N,K;
			M=sc.nextInt();
			N=sc.nextInt();
			K=sc.nextInt();
			
			int[][] map=new int[N][M];
			for(int i=0;i<N;i++) {
				Arrays.fill(map[i], 0);
			}
			
			for(int i=0;i<K;i++) {
				int x=sc.nextInt();
				int y=sc.nextInt();
				
				map[y][x]=1;
			}
			
			/*for(int i=0;i<N;i++) {
				for(int j=0;j<M;j++) {
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
			
			System.exit(1);*/
			
			// logic //
			int ans=0;
			for(int i=0;i<N;i++) {
				for(int j=0;j<M;j++) {
					if(map[i][j]==1) {
						ans+=1;
						map[i][j]=0;
						dfs(i,j,map,N,M);
					}
				}
			}
			System.out.println(ans);
		}
	}
}