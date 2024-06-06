package silver.solvedAc_18110;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	static int N, sum, startPoint, 
			arr[];
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N];

		for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(br.readLine());
		Arrays.sort(arr);
		
		startPoint = (int)(N * 0.15 + 0.5);
		for (int i = startPoint; i < N-startPoint; i++)	sum += arr[i];
		
		System.out.println((int)(1.0*sum/(N-startPoint*2) + 0.5));
		
	}

}
