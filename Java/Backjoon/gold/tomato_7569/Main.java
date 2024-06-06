package gold.tomato_7569;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, M, H, nr, nc, nh, tmp, cnt0;
	static int arr[][][], tmpArr[];
	static int dr[] = { 1, 0, -1, 0, 0, 0 }, dc[] = { 0, 1, 0, -1, 0, 0 }, dh[] = { 0, 0, 0, 0, 1, -1 };
	static Queue<int[]> q = new ArrayDeque<int[]>();
	static boolean vst[][][];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr = new StringTokenizer(br.readLine());
		M = Integer.parseInt(sr.nextToken());
		N = Integer.parseInt(sr.nextToken());
		H = Integer.parseInt(sr.nextToken());

		arr = new int[N][M][H];
		vst = new boolean[N][M][H];

		for (int k = 0; k < H; k++) {
			for (int i = 0; i < N; i++) {
				sr = new StringTokenizer(br.readLine());
				for (int j = 0; j < M; j++) {
					tmp = Integer.parseInt(sr.nextToken());
					arr[i][j][k] = tmp;
					if (tmp == 1) {
						q.offer(new int[] { i, j, k, 0 });
						vst[i][j][k] = true;
					}else if(tmp == 0) cnt0++;
				}
			}
		}
		
		bfs();
	}

	private static void bfs() {
		while (!q.isEmpty()) {
			tmpArr = q.poll();
			for(int i = 0; i < 6; i++) {
				nr = tmpArr[0] + dr[i];
				nc = tmpArr[1] + dc[i];
				nh = tmpArr[2] + dh[i];
				if (0<=nr && nr<N && 0<=nc && nc<M && 0<=nh && nh<H && !vst[nr][nc][nh] && arr[nr][nc][nh] == 0) {
					vst[nr][nc][nh] = true;
					cnt0--;
					q.offer(new int[] {nr, nc, nh, tmpArr[3]+1});
				}
			}
		}
		if(cnt0 == 0)System.out.println(tmpArr[3]);
		else System.out.println(-1);

	}

}
