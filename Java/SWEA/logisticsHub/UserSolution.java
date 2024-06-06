package logisticsHub;

import java.util.*;

class UserSolution {

	class Edge implements Comparable<Edge>{

		int to;
		int weight;

		public Edge(int to, int weight) {
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return this.weight - o.weight;
		}
	}

	TreeMap<Integer, List<Edge>> graph, revGraph;
	TreeMap<Integer, Integer> dist;
	Set<Integer> cities;
	PriorityQueue<Edge> pq;
	Edge now;

	public int init(int N, int sCity[], int eCity[], int mCost[]) {

		graph = new TreeMap<>();
		revGraph = new TreeMap<>();

		for (int i = 0; i < N; i++) {
			if(!graph.containsKey(sCity[i])){
				graph.put(sCity[i], new ArrayList<>());
			}
			graph.get(sCity[i]).add(new Edge(eCity[i], mCost[i]));

			if(!revGraph.containsKey(eCity[i])){
				revGraph.put(eCity[i], new ArrayList<>());
			}
			revGraph.get(eCity[i]).add(new Edge(sCity[i], mCost[i]));
		}

		cities = graph.keySet();

		return cities.size();
	}

	public void add(int sCity, int eCity, int mCost) {
		graph.get(sCity).add(new Edge(eCity, mCost));
		revGraph.get(eCity).add(new Edge(sCity, mCost));
	}

	public int cost(int mHub) {
		int res = 0;

		dist = new TreeMap<>();

//		정방향 연산
		for( int city : cities){
			dist.put(city, 999);
		}
		pq = new PriorityQueue<>();
		pq.offer(new Edge(mHub, 0));
		dist.put(mHub, 0);

		while(!pq.isEmpty()){
			now = pq.poll();

			for(Edge next : graph.get(now.to)){
				if (dist.get(next.to) > now.weight + next.weight){
					dist.put(next.to, now.weight + next.weight);
					pq.offer(new Edge(next.to, now.weight + next.weight));
				}
			}
		}
		for(int dist : dist.values()){
			res += dist;
		}

//		역방향 연산
		for( int city : cities){
			dist.put(city, 999);
		}
		pq = new PriorityQueue<>();
		pq.offer(new Edge(mHub, 0));
		dist.put(mHub, 0);

		while(!pq.isEmpty()){
			now = pq.poll();

			for(Edge next : revGraph.get(now.to)){
				if (dist.get(next.to) > now.weight + next.weight){
					dist.put(next.to, now.weight + next.weight);
					pq.offer(new Edge(next.to, now.weight + next.weight));
				}
			}
		}
		for(int dist : dist.values()){
			res += dist;
		}
		return res;
	}
}