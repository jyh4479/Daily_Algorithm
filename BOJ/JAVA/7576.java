import java.util.*;

public class main {
	public static void Main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int M=sc.nextInt();
		int N=sc.nextInt();
		
		int map[][]=new int[N][M];
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				map[i][j]=sc.nextInt();
			}
		}
		
		// logic //
		int[] dictx= {0,0,1,-1};
		int[] dicty= {1,-1,0,0};
		
		Queue<Integer> qx = new LinkedList<Integer>();
		Queue<Integer> qy = new LinkedList<Integer>();
		
		for(int i=0;i<N;i++) //토마토 좌표 체크
			for(int j=0;j<M;j++) {
				if(map[i][j]==1) {
					qx.add(j);
					qy.add(i);
				}
			}
		
		while(!qx.isEmpty() && !qy.isEmpty()) { //BFS
			int x=qx.poll();
			int y=qy.poll();
			
			for(int i=0;i<4;i++) {
				int dx=x+dictx[i];
				int dy=y+dicty[i];
				
				if(dx<0 || dy<0 || dx>=M || dy>=N) continue;
				else {
					if(map[dy][dx]==0) {
						qx.add(dx);
						qy.add(dy);
						map[dy][dx]=map[y][x]+1;
					}
				}
			}
		}
		
		/*for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				System.out.print(map[i][j]+" ");
			}
			System.out.println();
		}*/
		
		int ans=Integer.MIN_VALUE;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if(map[i][j]==0) {
					ans=-1;
					break;
				}
				
				if(map[i][j]!=-1) {
					ans=Math.max(ans, map[i][j]);
				}
			}
			if(ans==-1) break;
		}
		
		if(ans==-1) System.out.println(-1);
		else System.out.println(ans-1);
	}
}