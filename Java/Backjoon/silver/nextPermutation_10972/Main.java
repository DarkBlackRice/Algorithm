package silver.nextPermutation_10972;

import java.util.Scanner;

public class Main {

	static int N, input[];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		input = new int[N];

		for (int i = 0; i < N; i++) {
			input[i] = sc.nextInt();
		}

		sc.close();
		
		if(np(input)) {
			for (int i=0; i<N-1; i++) {
				System.out.print(input[i]);
				System.out.print(' ');
			}
			System.out.print(input[N-1]);
		}else System.out.println(-1);
		
	
	}

	private static boolean np(int[] perm) {
		int N = perm.length;
		
		int i = N-1;
		while(i > 0  && perm[i-1] >= perm[i]) i--;
		
		if (i==0) return false;
		
		int j = N-1;
		while(perm[i-1]>=perm[j]) j--;
		
		swap(perm, i-1, j);
		int k = N-1;
		while (i<k) {
			swap(perm, i++, k--);
		}
		
		return true;
	}
	
	private static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;

	}
}
