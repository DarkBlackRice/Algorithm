package gold.AC_5430;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	static int T, n, m, tmp;
	static boolean rev;
	static ArrayDeque<Integer> deque;
	static String func, data;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer sr;
		
		T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {

			rev = false;
			deque = new ArrayDeque<Integer>();

			func = br.readLine();
			n = Integer.parseInt(br.readLine());
			sr = new StringTokenizer(br.readLine(), "[],");
			for (int j = 0; j<n; j++) {
				deque.offer(Integer.parseInt(sr.nextToken()));
			}

//			System.out.println(Arrays.toString(deque.toArray()));
			solution();

		}

	}

	private static void solution() {

		StringBuilder sb = new StringBuilder();

//		주어진 함수의 길이만큼 반복문 실행
		m = func.length();
		for (int i = 0; i < m ; i++) {
//			만약 R이 들어왔다면 토글 : false면 정방향, true면 역방향
			if (func.charAt(i) == 'R')
				rev ^= true;

//			만약 D가 들어왔다면
			else {
//				deque.isEmpty() 상태에서는 새 스트링빌더 선언하여 오류메세지 넣고 반복종료
				if (deque.isEmpty()) {
					System.out.println("error");
					return;
				}
//				아닌 경우, 정방향 역방향에 따라 데이터를 뽑아주기만 한다 (저장하거나 하지 않는다)
				if (rev)
					deque.pollLast();
				else
					deque.pollFirst();
			}

		}

//		반복문이 다 끝나면 결과를 출력
//		우선 결과 만들기 전에 앞 뒤로 대괄호 넣기
		sb.append('[');
//		deque의 크기가 0보다 큰경우에만 아래를 실행하자.
		if(deque.size()>0) {
			
//			만약 rev가 true라면 역방향으로 문자열 빌드, 반대라면 정방향 문자열 빌드
			if (rev) {
				sb.append(deque.pollLast());
				while (!deque.isEmpty()) {
					sb.append(',').append(deque.pollLast());
				}
			} else {
				sb.append(deque.pollFirst());
				while (!deque.isEmpty()) {
					sb.append(',').append(deque.pollFirst());
				}
			}
		}

		sb.append(']');

		System.out.println(sb.toString());
		return;
	}

}
