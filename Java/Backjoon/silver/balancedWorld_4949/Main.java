package silver.balancedWorld_4949;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	
	static String temp;
	static Stack<Character> stack;
	static boolean isBalanced;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		temp = br.readLine();
				
		while(temp.charAt(0) != '.') {
			
			stack = new Stack<>();
			isBalanced = true;
			
			for(int i = 0; i<temp.length() ; i++) {
				if(temp.charAt(i) == '(' || temp.charAt(i) == '[') {
					stack.push(temp.charAt(i));
				}else if(temp.charAt(i) == ')') {
					if(stack.isEmpty() || stack.pop() != '(') {
						isBalanced=false;
						break;
					}
				}else if(temp.charAt(i) == ']') {
					if(stack.isEmpty() || stack.pop() != '[') {
						isBalanced=false;
						break;
					}
				}				
			}
			
			System.out.println(isBalanced && stack.isEmpty()? "yes":"no");
			temp = br.readLine();
		}

	}

}
