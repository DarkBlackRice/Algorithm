package gold.findMedian_2696;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static int tc, M, stdNum, num1, num2, ans, inputArr[];
	static PriorityQueue<Integer> minNums, maxNums;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb;
		
		tc = Integer.parseInt(br.readLine());
		
		while(tc-->0) {
			
			M = Integer.parseInt(br.readLine());
			sb = new StringBuilder();
			
			inputArr = new int[M];
			for(int i = 0; i < 1 + M/10; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 10; j++) {
					if(!st.hasMoreTokens()) break;
					inputArr[10*i + j] = Integer.parseInt(st.nextToken());
				}
			}
			

			minNums = new PriorityQueue<>(Collections.reverseOrder());
			maxNums = new PriorityQueue<>();
			
			stdNum = inputArr[0];
			sb.append(stdNum).append(' ');
			
			
			for (int i = 1; i < M; i += 2) {
				
//				작은 값이 num1, 큰 값이 num2
				if(inputArr[i] > inputArr[i+1]) {
					num2 = inputArr[i];
					num1 = inputArr[i+1];
				}else {
					num1 = inputArr[i];
					num2 = inputArr[i+1];
				}
				
				if (stdNum < num1) {
					
					minNums.offer(stdNum);
					maxNums.offer(num1);
					maxNums.offer(num2);
					stdNum = maxNums.poll();
					
					
				}else if (stdNum > num2) {
					
					maxNums.offer(stdNum);
					minNums.offer(num1);
					minNums.offer(num2);
					stdNum = minNums.poll();
					
				}else {
					
					minNums.offer(num1);
					maxNums.offer(num2);
					
				}
				
				sb.append(stdNum);
				if(i%20 == 17) sb.append('\n');
				else sb.append(' ');
				
			}
			ans = 1 + M/2;
			System.out.println(ans);
			System.out.println(sb.toString());
			
		}

	}

}
