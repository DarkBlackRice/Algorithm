package silver.queue_10845;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	static int N, num;
	static String input;
	static Deque<Integer> deque = new ArrayDeque<>();
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			input = st.nextToken();
			if(st.hasMoreTokens()) num = Integer.parseInt(st.nextToken());
			
			if(input.equals("push")) deque.offer(num);
			else if(input.equals("pop")) {
				if(deque.isEmpty()) sb.append(-1).append('\n');
				else sb.append(deque.poll()).append('\n');
			}
			else if(input.equals("size")) sb.append(deque.size()).append('\n');
			else if(input.equals("empty")) {
				if(deque.isEmpty())sb.append(1).append('\n');
				else sb.append(0).append('\n');
			}
			else if(input.equals("front")) {
				if(deque.isEmpty()) sb.append(-1).append('\n');
				else sb.append(deque.peekFirst()).append('\n');
			}
			else if(input.equals("back")) {
				if(deque.isEmpty()) sb.append(-1).append('\n');
				else sb.append(deque.peekLast()).append('\n');
			}
		}
		
		System.out.println(sb.toString());
		
	}

}
