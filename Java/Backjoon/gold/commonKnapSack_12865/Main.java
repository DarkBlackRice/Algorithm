package gold.commonKnapSack_12865;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N, K, w, v;
	static int dp[];

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		dp = new int[K+1];

		for (int i = 0; i < N; i++) {
		
			st = new StringTokenizer(br.readLine());
			w = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			
			for (int j = K; j>= w; j--) {
				dp[j] = Math.max(dp[j-w] + v, dp[j]);
			}
			
		}
		
		System.out.println(Arrays.toString(dp));

	}

}
