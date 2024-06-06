package silver.needFriends_21736;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, M, nr, nc;
	static int ans = 0;
	static int coord[] = { 0, 0 };
	static String temp;
	static int dr[] = { 0, 1, 0, -1 };
	static int dc[] = { 1, 0, -1, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr = new StringTokenizer(br.readLine());
		N = Integer.parseInt(sr.nextToken());
		M = Integer.parseInt(sr.nextToken());

		char arr[][] = new char[N][M];
		for (int i = 0; i < N; i++) {
			temp = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = temp.charAt(j);
			}
		}

		coord = findStart(arr, N, M);
		bfs(arr, N, M, coord[0], coord[1]);
		if (ans > 0) {
			System.out.println(ans);
		} else {
			System.out.println("TT");
		}

	}

	public static int[] findStart(char[][] arr, int N, int M) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] == 'I') {
					coord[0] = i;
					coord[1] = j;
					return coord;
				}
			}
		}
		return coord;
	}

	public static void bfs(char[][] arr, int N, int M, int sr, int sc) {
		Queue<int[]> q = new ArrayDeque<>();
		boolean visited[][] = new boolean[N][M];
		visited[sr][sc] = true;
		coord[0] = sr;
		coord[1] = sc;
		q.add(coord);
		while (!q.isEmpty()) {
			coord = q.poll();
			for (int i = 0; i < 4; i++) {
				nr = coord[0] + dr[i];
				nc = coord[1] + dc[i];
				if (0 <= nr && nr < N && 0 <= nc && nc < M && !visited[nr][nc] && arr[nr][nc] != 'X') {
					visited[nr][nc] = true;
					if (arr[nr][nc] == 'P')
						ans++;
//					배열을 만들어서 쓸려면, 매번 새로운 배열을 선언해서 넣어줘야한다! 안 그러면 데이터가 새로 써진다!
					q.add(new int[] {nr, nc});
				}
			}
		}

	}
}
