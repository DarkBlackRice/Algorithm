package bronze.stringStudy_1157;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr = new StringTokenizer(br.readLine());
		String str = sr.nextToken().toUpperCase();
		int[] cnt = new int[26];
		int N = str.length();
		for (int i = 0; i < N; i++) {
			cnt[str.charAt(i) - 'A']++;
		}
		int ans = 0;
		boolean dup = false;
		for (int i = 0; i < 26; i++) {
			if (cnt[i] >= cnt[ans]) {
				if (i != 0 && cnt[i] == cnt[ans]) {
					dup = true;
				}else {
					dup = false;
					ans = i;
				}
			}
		}
		if (dup) {
			System.out.println((char)'?');
		}else {
			System.out.println((char)(ans+'A'));
		}

	}

}
