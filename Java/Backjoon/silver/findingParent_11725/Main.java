package silver.findingParent_11725;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	static int N, from, to;
	static int parent[];
	static ArrayList<Integer>[] adj;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		parent = new int[N+1];
		adj = new ArrayList[N+1];
		for (int i = 0; i < N+1; i++) {
			adj[i] = new ArrayList<Integer>();
		}
		
		for (int i = 0; i < N-1; i++) {
			st = new StringTokenizer(br.readLine());
			from = Integer.parseInt(st.nextToken());
			to = Integer.parseInt(st.nextToken());
			adj[from].add(to);
			adj[to].add(from);			
		}
		
		preorder(1);
		
		StringBuilder sb = new StringBuilder();
		for (int i = 2; i < N+1; i++) {
			sb.append(parent[i]).append('\n');
		}
		
		System.out.println(sb);
	}
	
	static void preorder(int now) {
		for (Integer i : adj[now]) {
			if(parent[now] == i || parent[i] != 0) continue;
			parent[i] = now;
			preorder(i);
		}
	}

}
