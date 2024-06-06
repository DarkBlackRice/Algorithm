package bronze.numOfWords_1152;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		try {
			StringTokenizer sr = new StringTokenizer(br.readLine());
			System.out.println(sr.countTokens());
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
