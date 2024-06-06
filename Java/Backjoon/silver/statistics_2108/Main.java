package silver.statistics_2108;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	
	static int N, tmp, sum = 0, avg, mode = -1,
			
			min=Integer.MAX_VALUE, max=Integer.MIN_VALUE;
	static int cnt[] = new int[8003], arr[];
	static ArrayList<Integer> modList = new ArrayList<>();

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		
		for (int i=0; i<N; i++) {
			tmp = Integer.parseInt(br.readLine());
//			Áß¾Ó°ª
			arr[i] = tmp;
//			Æò±Õ
			sum += tmp;
//			ÃÖºó°ª
			cnt[tmp+4000]++;
//			¹üÀ§
			if (min > tmp) min=tmp;
			if (max < tmp) max=tmp;
		}
		
//		Æò±Õ Ãâ·Â
		if (sum>=0) System.out.println((int)(1.0*sum/N + 0.5));
		else System.out.println((int)(1.0*sum/N - 0.5));
		
//		Áß¾Ó°ª Ãâ·Â
		Arrays.sort(arr);
		System.out.println(arr[N/2]);
		
//		ÃÖºó°ª Ãâ·Â
		for(int i = 0; i<8003; i++) {
			tmp = cnt[i];
			
			if (tmp == 0) continue;
			
			if (mode < tmp) {
				modList = new ArrayList<>();
				modList.add(i);
				mode = tmp;
			}else if(mode == tmp)
				modList.add(i);
		}
		if(modList.size()>1) System.out.println(modList.get(1)-4000);
		else System.out.println(modList.get(0)-4000);
		
//		¹üÀ§ Ãâ·Â
		System.out.println(max-min);
		
	}

}
