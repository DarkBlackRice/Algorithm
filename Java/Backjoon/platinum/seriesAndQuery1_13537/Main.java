package platinum.seriesAndQuery1_13537;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M;
    static int[] arr;
    static int[][] mergeSortTree;

    public static int[] merge(int[] arr1, int[] arr2){
        int len1 = arr1.length;
        int len2 = arr2.length;
        int len = len1 + len2;

        int idx, i, j;
        idx = i = j = 0;

        int[] res = new int[len];
        while(idx < len){
            if (j == len2 || (i < len1 && (arr1[i] < arr2[j]))) {
                res[idx++] = arr1[i++];
            } else {
                res[idx++] = arr2[j++];
            }
        }
        return res;
    }

    public static void init(int node, int start, int end){

        mergeSortTree[node] = new int[end - start + 1];

        if (start == end) {
            mergeSortTree[node] = new int[]{arr[start]};
            return;
        }

        int mid = (start + end) / 2;
        init(node*2, start, mid);
        init(node*2+1, mid+1, end);

        mergeSortTree[node] = merge(mergeSortTree[node * 2], mergeSortTree[node * 2 + 1]);
    }

    public static int upperBound(int node, int value){
        int start = 0;
        int end = mergeSortTree[node].length;
        int mid;
        while(start < end){
            mid = (start + end) / 2;
            if (mergeSortTree[node][mid] <= value) {
                start = mid + 1;
            }else{
                end = mid;
            }
        }

        return end;
    }

    public static int numOfLargerNums(int node, int start, int end, int qStart, int qEnd, int value) {

//      완전 미포함
        if(end < qStart || qEnd < start) return 0;
//      완전 포함
        if (qStart <= start && end <= qEnd) {
//           어퍼바운드 구하는 함수 구현
            return mergeSortTree[node].length - upperBound(node, value);
        }
//      그 외
        int mid = (start + end) / 2;

        return numOfLargerNums(node*2, start, mid, qStart, qEnd, value) +
                numOfLargerNums(node*2+1, mid+1,end, qStart, qEnd, value);

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        arr = new int[N+1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N+1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

//      트리 초기화
        mergeSortTree = new int[4 * N][];
        init(1, 1, N);

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int qStart = Integer.parseInt(st.nextToken());
            int qEnd = Integer.parseInt(st.nextToken());
            int value = Integer.parseInt(st.nextToken());

            sb.append(numOfLargerNums(1, 1, N, qStart, qEnd, value)).append('\n');
        }

        System.out.println(sb);
    }
}
