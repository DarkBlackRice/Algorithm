package gold.countingOnes_9527;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static long ones(long num){
        long cnt = 0L;
        long sum = 0L;

        for (int i = 60; i > 0; i--) {
            if((num & (1L<<i)) != 0L){
                sum += dp[i - 1] + 1 + (cnt++ * (1L << i));
            }
        }

        sum += num % 2 * (cnt + 1);
        return sum;
    }

    static long[] dp;
    static long A, B;

    public static void main(String[] args) throws IOException {
        dp = new long[64];
        dp[0] = 1L;
        for (int i = 1; i <= 60; i++) {
            dp[i] = (dp[i - 1] * 2) + (1L << i);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());

//        System.out.println(ones(B));
//        System.out.println(ones(A-1));
        System.out.println(ones(B) - ones(A - 1));
    }
}
