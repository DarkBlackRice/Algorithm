package gold.MST_1197;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{
	
//	간선 클래스 선언
	static class Edge implements Comparable<Edge>{
		int from, to, weight ;

		public Edge(int cur, int next, int weight) {
			super();
			this.from = cur;
			this.to = next;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
	}
	
//	필요한 서로소 집합 메서드 정의하기
	private static void makeSet() {
		parent = new int[V+1];
		for (int i = 1; i < V+1; i++) {
			parent[i] = i;
		}
	}
	
	private static int find(int x) {
		if(parent[x] == x) return x;
		return parent[x] = find(parent[x]);
	}
	
	private static boolean union(int x, int y) {
		int	xRoot = find(x);
		int yRoot = find(y);
		if(xRoot == yRoot) return false;
		parent[yRoot] = xRoot;
		return true;
	}
	
	
	static int V, E, from, to, weight, cnt=0, result=0;
	static int parent[];
	static Edge edgeList[];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		edgeList = new Edge[E];
		
		
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			from = Integer.parseInt(st.nextToken());
			to = Integer.parseInt(st.nextToken());
			weight = Integer.parseInt(st.nextToken());
			edgeList[i] = new Edge(from,to,weight);
		}
		
		Arrays.sort(edgeList);
		makeSet();
		
		
		for (Edge edge : edgeList) {
			if (union(edge.from, edge.to)) {
				result += edge.weight;
				if (++cnt == V-1) break;
			} 
			
		}
		
		System.out.println(result);
		
	}

}
