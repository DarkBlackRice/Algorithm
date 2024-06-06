package silver.atob_16953;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int a, b, cnt = 1;
	static boolean success;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		
		while(b>=a) {
			if(b%2 == 0) {
				b /= 2;
			}else if(b%10 == 1) {
				b /= 10;
			}else break;
			cnt ++;
			if(b == a) {
				success = true;
				break;
			}
		}
		
		System.out.println(success? cnt:-1);
		
	}

}
