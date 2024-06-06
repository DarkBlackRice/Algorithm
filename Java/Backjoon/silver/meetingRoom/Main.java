package silver.meetingRoom;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

	static int N, st, et, cnt = 0, nowEndTime = 0;
	static int[] nextTime;
	static ArrayList<int[]> arr;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr = new StringTokenizer(br.readLine());
		N = Integer.parseInt(sr.nextToken());
		arr = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			sr = new StringTokenizer(br.readLine());
			st = Integer.parseInt(sr.nextToken());
			et = Integer.parseInt(sr.nextToken());
			arr.add(new int[] {st, et});
		}
		
		Comparator<int[]> index1 = new Comparator<int[]>(){
			@Override
			public int compare(int[] o1, int[] o2) {
				if (o1[1] == o2[1]) return o1[0] - o2[0];
				return o1[1] - o2[1];
			}
		};
		
		Collections.sort(arr, index1);
		
		for (int i = 0; i < N; i++) {
			nextTime = arr.get(i);
			if (nowEndTime <= nextTime[0]) {
				cnt++;
				nowEndTime = nextTime[1];
			}
		}
		System.out.println(cnt);
	}

}
