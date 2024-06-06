package silver.IOIOI_5525;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int N, M, pattLen, tmpLen, ans = 0;
	static boolean isI;
	static String arr;

	public static void main(String[] args) throws NumberFormatException, IOException {

//		0. 데이터 input받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		pattLen = 2*N + 1;
		arr = br.readLine();
		
		int i = 0;
		while(i<M) {
			isI = true;
			tmpLen = 0;
			while(i<M) {
				if((isI && arr.charAt(i)=='O') || (!isI && arr.charAt(i)=='I')) {
					break;
				}
				i++;
				isI ^= true;
				tmpLen ++;
				
			}
			if(tmpLen >= pattLen) ans += (tmpLen-pattLen)/2 + 1;
			if(tmpLen == 0)i++;
		}
		
		System.out.println(ans);
	}

}
