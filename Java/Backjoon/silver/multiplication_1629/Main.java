package silver.multiplication_1629;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static long a, b, c;
	static long memo[] = new long[50];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		
		a %= c;
		Arrays.fill(memo, -1L);
		System.out.println(power(a, b, c, 0));
		
	}
	
	private static long power(long x, long y, long z, int k) {
		
		if (y == 1) return x;
		
		else if(y % 2 == 0) {
			if (memo[k] != -1) return memo[k];
			else{
				long tmp = power(x, y/2, z, k+1) * power(x, y/2, z, k+1);
				long ans =  tmp % z;
				return memo[k] = ans;
			}
		}
		
		else {
			if (memo[k] != -1) return memo[k];
			else {
				long tmp = (power(x, y/2, z, k+1) * power(x, y/2, z, k+1))%z * x;
				long ans =  tmp % z;
				return memo[k] = ans;
			}
		}

	}

}
