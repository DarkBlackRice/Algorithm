package silver.stepOver_2579;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int arr[], dp[], N;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		if(N==1) {
			System.out.println(arr[0]);
			return;
			
		}else if(N==2) {
			System.out.println(arr[0]+arr[1]);
			return;
			
		}else {
//			2*N 길이의 배열에서, 홀수 인덱스에는 L(longTerm)데이터를,짝수 인덱스에는 S(ShortTerm)데이터를 넣자.
			
//			dp 초기화 작업
			dp = new int[2*N];
			dp[0] = dp [1] = arr[0];
			dp[2] = arr[1];
			dp[3] = arr[0] + arr[1];
			
			for (int i = 2; i<N; i++) {
				dp[2*i+1] = arr[i] + dp[2*(i-1)];
				if (dp[2*(i-2)] > dp[2*(i-2)+1]) {
					dp[2*i] = arr[i] + dp[2*(i-2)];
				}else {
					dp[2*i] = arr[i] + dp[2*(i-2)+1];
				}
			}
			
			if(dp[2*(N-1)]>dp[2*(N-1)+1]) {
				System.out.println(dp[2*(N-1)]);
			}else {
				System.out.println(dp[2*(N-1)+1]);
			}	
		}	
	}	
}