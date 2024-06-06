package silver.numberCard2_10816;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;

public class Main {
	
	static int N, M;
	static String temp;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		HashMap<String, Integer> map = new HashMap<>();
		
		for (int i = 0; i < N; i++) {
			temp = st.nextToken();
			map.put(temp, map.getOrDefault(temp, 0)+1);
		}
		
		StringBuilder sb = new StringBuilder();
		M = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		sb.append(map.getOrDefault(st.nextToken(), 0));
		for (int i = 0; i < M-1; i++) {
			temp = st.nextToken();
			sb.append(' ').append(map.getOrDefault(temp, 0));
		}
		
		System.out.println(sb.toString());
		
	}

}
