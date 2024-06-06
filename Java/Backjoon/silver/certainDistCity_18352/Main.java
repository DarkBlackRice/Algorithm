package silver.certainDistCity_18352;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node implements Comparable<Node>{
		int vertex, weight;
		Node next;
		
		public Node(int vertex, Node next) {
			this(vertex, 1, next);
			
		}
		public Node(int vertex, int weight, Node next) {
			this.vertex = vertex;
			this.next = next;
			this.weight = weight;
		}
		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}
		
		
		
	}
	
	static void dijkstra(int start) {
		dist = new int[N+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start] = 0;
		q.offer(new Node(start, dist[start], nodeList[start]));
		while(!q.isEmpty()) {
			now = q.poll();
			next = now.next;
			while(next != null) {
				if(dist[next.vertex] > now.weight+next.weight) {
					dist[next.vertex] = now.weight + next.weight;
					q.offer(new Node(next.vertex, dist[next.vertex], nodeList[next.vertex]));
				}
				next = next.next;
			}
			
		}
		
	}
	
	
	static int N, M, K, X, from, to;
	static boolean flag=true;
	static int dist[];
	static Node now, next;
	static Node nodeList[];
	static PriorityQueue<Node> q = new PriorityQueue<>();

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
		
//		인접리스트 (연결리스트로 구현) 만들기!
		nodeList = new Node[N+1];
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			from = Integer.parseInt(st.nextToken());
			to = Integer.parseInt(st.nextToken());
			nodeList[from] = new Node(to, nodeList[from]);
		}
		
//		다익스트라 (X 출발)
		dijkstra(X);
				
//		dist 배열을 돌면서 값이 K인 index 출력하기
		for(int i = 1; i<N+1; i++) {
			if(dist[i] == K) {
				System.out.println(i);
				flag = false;
			}
		}
		if (flag) System.out.println(-1);

	}

}
