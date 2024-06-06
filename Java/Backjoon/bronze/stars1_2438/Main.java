package bronze.stars1_2438;


import java.util.Scanner;

public class Main {

	static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		sc.close();		
		for (int i = 1; i < N + 1; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print('*');
			}
			System.out.println();
		}

	}

}
