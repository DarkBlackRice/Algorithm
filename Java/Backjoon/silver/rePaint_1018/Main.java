package silver.rePaint_1018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, M, tmp1, tmp2;
	static String temp;
	static char arr[][];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		arr = new char[N][M];

		for (int i = 0; i < N; i++) {
			temp = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = temp.charAt(j);
			}
		}

		for (int i = 0; i < N - 7; i++) {
			for (int j = 0; j < M - 7; j++) {
				for(int k = i; k<i+8; k++) {
					tmp1 = 0;
					tmp2 = 0;
//					for(int m=)
				}
			}
		}

	}

}
