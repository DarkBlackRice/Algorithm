package silver.unheard_1764;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static HashSet<String> unheard, unseen;
	static Object ans[];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		unheard = new HashSet<>();
		unseen = new HashSet<>();
		
		for (int i = 0; i < N; i++) {
			unheard.add(br.readLine());
		}
		for (int i = 0; i < M; i++) {
			unseen.add(br.readLine());
		}
		unheard.retainAll(unseen);
		ans = unheard.toArray(new String[0]);
		Arrays.sort(ans);
		System.out.println(ans.length);
		for (Object str: ans) {
			System.out.println(str);
		}
		
	}

}
