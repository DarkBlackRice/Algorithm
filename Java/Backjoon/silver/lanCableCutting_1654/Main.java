package silver.lanCableCutting_1654;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, K, tmp;
	static long ans, max = 0;
	static int arr[], dist[];

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		K = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());

		arr = new int[K];
		dist = new int[K];

		for (int i = 0; i < K; i++) {
			tmp = Integer.parseInt(br.readLine());
			arr[i] = tmp;
			if (max < tmp) max = tmp;
		}
		
		binarySearch(1, max);
		System.out.println(ans);
	}
	
	private static void binarySearch(long start, long end) {
		
		if (start > end) return;
		
		long mid = (start+end) / 2;
		tmp = 0;
		for (int i = 0; i < K; i++) {
			tmp += arr[i] / mid;
		}
		if (tmp >= N) {
			ans = mid;
			binarySearch(mid+1, end);
		}else {
			binarySearch(start, mid-1);
		}
	}

}
