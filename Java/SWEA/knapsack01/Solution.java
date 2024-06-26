package knapsack01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int tc, v, c, N, K;
	static int dp[];

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		tc = Integer.parseInt(br.readLine());

		for (int k = 1; k <= tc; k++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			dp = new int[K + 1];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				v = Integer.parseInt(st.nextToken());
				c = Integer.parseInt(st.nextToken());

				for (int j = K; j >= v; j--) {

					if (dp[j] < dp[j - v] + c)
						dp[j] = dp[j - v] + c;

				}

			}

			System.out.println("# " + k + ' ' + dp[K]);
		}

	}

}
