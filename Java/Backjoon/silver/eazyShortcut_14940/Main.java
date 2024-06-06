package silver.eazyShortcut_14940;

import java.io.*;
import java.util.*;

public class Main {

	static int n, m, tmp, sr, sc, nr, nc;
	static int coord[], arr[][], vst[][];
	static int dr[] = { 0, 1, 0, -1 };
	static int dc[] = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer str = new StringTokenizer(br.readLine());

		n = Integer.parseInt(str.nextToken());
		m = Integer.parseInt(str.nextToken());
		arr = new int[n][m];
		vst = new int[n][m];
		
		for (int i=0; i<n; i++) Arrays.fill(vst[i], -1);
//		초기화에 대한 고민이 필요하다. (도달못하면 -1, 원래 못 가면 0)
		
		for (int i = 0; i < n; i++) {
			str = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				tmp = Integer.parseInt(str.nextToken());
				arr[i][j] = tmp;
				if (tmp == 2) {
					sr = i;
					sc = j;
				} else if (tmp == 0) {
					vst[i][j] = 0;
				}
			}
		}
		
		bfs(sr, sc);
		StringBuilder sb = new StringBuilder();
		for (int[] temp : vst) {
			for (int j = 0; j < m; j++) {
				sb.append(temp[j]).append(' ');
			}
			sb.append('\n');

		}
		
		System.out.println(sb.toString());

	}

	private static void bfs(int sr, int sc) {
		Queue<int[]> q = new ArrayDeque<int[]>();
		q.offer(new int[] { sr, sc });
		vst[sr][sc] = 0;
		while (!q.isEmpty()) {
			coord = q.poll();
			for (int i = 0; i < 4; i++) {
				nr = coord[0] + dr[i];
				nc = coord[1] + dc[i];
				if (0 <= nr && nr < n && 0 <= nc && nc < m && vst[nr][nc] == -1 && arr[nr][nc] == 1) {
					vst[nr][nc] = vst[coord[0]][coord[1]] + 1;
					q.offer(new int[] {nr, nc});
				}
			}
		}

	}

}
