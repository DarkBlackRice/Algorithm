package gold.minimumCost_1916;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	
	static class Node implements Comparable<Node>{
		int now, weight;
		Node next;
				
		public Node(int now, int weight, Node next) {
			this.now = now;
			this.weight = weight;
			this.next = next;
		}

		public Node(int now, int weight) {
			this(now, weight, null);
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.weight, o.weight);
		}
		
	}

	static int N, M, f, t, w, start, end;
	static int dist[];
	static boolean vst[];
	static Node u, v, arr[];
	static PriorityQueue<Node> pq = new PriorityQueue<>();
	
	public static void main(String[] args) throws NumberFormatException, IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		arr = new Node[N+1];
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			f = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			arr[f] = new Node(t, w, arr[f]);
		}
		
		st = new StringTokenizer(br.readLine());
		start = Integer.parseInt(st.nextToken());
		end = Integer.parseInt(st.nextToken());

		dijkstra(start);
		System.out.println(dist[end]);

	}
	
	static void dijkstra(int start) {
		dist = new int[N+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		
		vst = new boolean[N+1];
		
		dist[start] = 0;
		pq.add(new Node(start, dist[start]));
		while (!pq.isEmpty()) {
			u = pq.poll();
			vst[u.now] = true;
			v = arr[u.now];
			while (v != null) {
				if(!vst[v.now] && dist[v.now] > v.weight + u.weight) {
					dist[v.now] = v.weight + u.weight;
					pq.add(new Node(v.now, v.weight+u.weight));
				}
				v = v.next;
			}
		}
		
	}

}
