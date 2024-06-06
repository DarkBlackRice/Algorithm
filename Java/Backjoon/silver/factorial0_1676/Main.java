package silver.factorial0_1676;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int N, cnt, tmp;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		cnt = 0;
		for (int i = 0; i <= N; i++) {
			tmp = i;
			while(tmp != 0 && tmp%5 == 0) {
				cnt ++;
				tmp /= 5;
			}
		}
		
		System.out.println(cnt);
		
	}

}
