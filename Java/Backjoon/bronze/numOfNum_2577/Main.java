package bronze.numOfNum_2577;


import java.util.Scanner;

public class Main {
	
	static int multi = 1, N;
	static String str;
	static int[] cnt = new int[10];
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i=0; i<3; i++) {
			multi = multi * sc.nextInt() ;
		}
		sc.close();
		str = String.valueOf(multi);
		N = str.length();
		
		for (int i = 0; i < N; i++) {
			cnt[str.charAt(i)-'0'] ++ ;
		}
		for (int n:cnt) {
			System.out.println(n);
		}
	}

}
