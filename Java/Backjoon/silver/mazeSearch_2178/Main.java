package silver.mazeSearch_2178;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, M, nr, nc;
	static int vst[][], coord[] = { 0, 0 }, dr[] = { 0, 1, 0, -1 }, dc[] = { 1, 0, -1, 0 };
	static char arr[][];
	static String temp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr = new StringTokenizer(br.readLine());
		N = Integer.parseInt(sr.nextToken());
		M = Integer.parseInt(sr.nextToken());
		arr = new char[N][M];
		vst = new int[N][M];

		for (int i = 0; i < N; i++) {
			temp = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = temp.charAt(j);
			}
		}


		System.out.println(bfs());
//		for(int i=0; i<N; i++)System.out.println(Arrays.toString(vst[i]));

	}

	private static int bfs() {
		Queue<int[]> q = new ArrayDeque<>();
		vst[0][0] = 1;
		q.add(new int[] {0,0});
		while (!q.isEmpty()) {
			coord = q.poll();
			for(int i=0; i<4; i++) {
				nr = coord[0] + dr[i];
				nc = coord[1] + dc[i];
				if (0<=nr && nr<N && 0<=nc && nc<M && vst[nr][nc] == 0 && arr[nr][nc] == '1') {
					vst[nr][nc] = vst[coord[0]][coord[1]] + 1;
					if(nr==N-1 && nc == M-1) return vst[nr][nc];
					q.add(new int[] {nr, nc});
				}
			}
		}
		return -1;
	}

}
