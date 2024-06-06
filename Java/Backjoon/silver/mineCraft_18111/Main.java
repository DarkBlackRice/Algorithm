package silver.mineCraft_18111;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

	static int N, M, B, tmp, maxHeight, block, ans;
	static int tgIndex, tgValue, nextValue, res1, res2;
	static ArrayList<Integer> list = new ArrayList<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		B = Integer.parseInt(st.nextToken());

		block = B;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				tmp = Integer.parseInt(st.nextToken());
				list.add(tmp);
				block += tmp;
			}
		}

		maxHeight = block / (N * M);
		Collections.sort(list);

//		2/3 지점의 값이 더 크면, 그냥 만들 수 있는 블럭 수로 만드는게 최선이야
		tgIndex = 2 * N * M / 3;
		tgValue = list.get(tgIndex);
		if (tgValue > maxHeight) {
			ans = cal(maxHeight);
			tgValue = maxHeight;
//		아니면, 경계값을 비교해야한단다
		} else {
			nextValue = list.get(tgIndex + 1);
			if (tgValue == nextValue) {
				ans = cal(tgValue);
			} else {
				res1 = cal(tgValue);
				res2 = cal(nextValue);
				if (res2 > res1) {
					tgValue = nextValue;
					ans = res2;
				}else {
					ans = res1;
				}
			}

		}
		
		System.out.print(ans);
		System.out.print(' ');
		System.out.println(tgValue);

	}

	private static int cal(int num) {
		int res = 0;
		for (int i = 0; i < list.size(); i++) {
			tmp = list.get(i) - num;
			if(tmp<0) {
				res += tmp*-1;
			}else {
				res += tmp*2;
			}
		}

		return res;
	}

}
