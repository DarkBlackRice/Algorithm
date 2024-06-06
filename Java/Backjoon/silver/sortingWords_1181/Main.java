package silver.sortingWords_1181;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
	
	static int N;
	static String tmp, strArr[];
	
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		strArr = new String[N];
		
		for (int i = 0; i < N; i++) {
			tmp = br.readLine();
			strArr[i] = tmp;
		}
		
		
		Arrays.sort(strArr, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				if(o1.length() == o2.length()) {
					return o1.compareTo(o2);
				}else {
					return o1.length() - o2.length();
				}
			}
		});
		
		System.out.println(strArr[0]);
		for (int i = 1; i < strArr.length; i++) {
			if(!strArr[i].equals(strArr[i-1])) {
				System.out.println(strArr[i]);
			}
		}
	}

}
