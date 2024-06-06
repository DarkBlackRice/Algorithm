package silver.longestSubSeries_11053;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, prev, tmp, ans = 0, tmpCnt, length = 0;
	static int arr[], dp[];

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		arr = new int[N];
		dp = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < N; i++) {
			tmp = arr[i];
			tmpCnt = dp[i] + 1;
			for (int j = i+1; j < N; j++) {
				if (tmp < arr[j] && dp[j] < tmpCnt) {
					dp[j] = tmpCnt;
				}
			}
		}

		for (int i = 0; i < N; i++) {
			tmp = dp[i];
			if (ans < tmp) ans = tmp;
		}
		
		System.out.println(ans+1);

	}

}
