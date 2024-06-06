package silver.stack_10828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

	static int N, num;
	static String input;
	static Stack<Integer> stack = new Stack<>();
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			input = st.nextToken();
			if(st.hasMoreTokens()) num = Integer.parseInt(st.nextToken());
			
			if(input.equals("push")) stack.push(num);
			else if(input.equals("pop")) {
				if(stack.isEmpty()) sb.append(-1).append('\n');
				else sb.append(stack.pop()).append('\n');
			}
			else if(input.equals("size")) sb.append(stack.size()).append('\n');
			else if(input.equals("empty")) {
				if(stack.isEmpty())sb.append(1).append('\n');
				else sb.append(0).append('\n');
			}
			else if(input.equals("top")) {
				if(stack.isEmpty()) sb.append(-1).append('\n');
				else sb.append(stack.peek()).append('\n');
			}
		}
		
		System.out.println(sb.toString());
		
	}

}
