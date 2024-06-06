package silver.printerQueue_1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int tc, N, M, tmp, priority, cnt, tgCnt, length;
	static int priorityArr[];
	static Queue<Integer> q;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		tc = Integer.parseInt(br.readLine());

		while (tc-- > 0) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			tgCnt = M;
			length = N-1;
			priorityArr = new int[10];
			q = new ArrayDeque<Integer>();
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				tmp = Integer.parseInt(st.nextToken());
				priorityArr[tmp]++;
				q.offer(tmp);
			}
			
			prioritySet();
			
			cnt = 1;
			while(!q.isEmpty()) {
				tmp = q.poll();
				if(tmp == priority) {
					if (tgCnt == 0) {
						System.out.println(cnt);
						break;
					}else {
						tgCnt--;
						length--;
						priorityArr[priority]--;
						cnt ++;
						prioritySet();						
					}
				}else {
					if (tgCnt == 0) {
						tgCnt = length;
					}else {
						tgCnt--;
					}
					q.offer(tmp);
				}
			}
			
		}

	}
	
	private static void prioritySet() {
		for(int i = 9; i > -1; i--) {
			if (priorityArr[i] != 0) {
				priority = i;
				return;
			}
		}
	}

}
