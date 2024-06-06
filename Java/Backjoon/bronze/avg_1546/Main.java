package bronze.avg_1546;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, sum=0, max=0, tmp;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			tmp = Integer.parseInt(st.nextToken());
			if(max < tmp) max = tmp;
			sum += tmp;
		}
		
		System.out.println(100.0*sum/(N*max));
	}

}
