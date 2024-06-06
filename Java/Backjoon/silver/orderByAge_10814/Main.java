package silver.orderByAge_10814;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	
	static class Person implements Comparable<Person>{
		int age;
		String name;
		
		public Person(int age, String name) {
			super();
			this.age = age;
			this.name = name;
		}

		@Override
		public int compareTo(Person o) {
			// TODO Auto-generated method stub
			return this.age - o.age;
		}
	}
	
	static int N, age;
	static String name;
	static Person arr[];
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new Person[N];
		
		
		StringTokenizer st;
		for (int i = 0; i < N; i++) {
			
			st = new StringTokenizer(br.readLine());
			age = Integer.parseInt(st.nextToken());
			name = st.nextToken();
			arr[i] = new Person(age, name);
			
		}
		
		StringBuilder sb = new StringBuilder();
		Arrays.sort(arr);
		for (Person person : arr) {
			sb.append(person.age).append(' ').append(person.name).append('\n');
		}
		System.out.println(sb.toString());

	}

}
