package platinum.seriesAndQuery21_16975;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N, M;
    static int[] arr;
    static long[] tree;
    static long result;

    public static void init(int node, int start, int end){
        if(start == end){
            tree[node] = arr[start];
            return;
        }
        int mid = (start + end) /2 ;

        init(
                node * 2,
                start,
                mid
        );

        init(
                node*2 + 1,
                mid+1,
                end
        );
    }

    public static void update(int node, int start, int end, int qStart, int qEnd, int value){
        if(qEnd < start || end < qStart){
            return;
        }

        if(qStart <= start && end <= qEnd){
            tree[node] += value;
            return;
        }

        int mid = (start + end) /2 ;

        update(
                node * 2,
                start,
                mid,
                qStart,
                qEnd,
                value
        );

        update(
                node*2 + 1,
                mid+1,
                end,
                qStart,
                qEnd,
                value
        );
    }

    public static void getInfo(int node, int start, int end, int qIndex){
        if(qIndex < start || end < qIndex){
            return;
        }

        if(start == end){
            result += tree[node];
            return;
        }

        result += tree[node];
        int mid = (start + end) /2;

        getInfo(
                node*2,
                start,
                mid,
                qIndex
        );

        getInfo(
                node*2 + 1,
                mid + 1,
                end,
                qIndex
        );

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        tree = new long[4*N];
        init(1, 1, N);
//        System.out.println(Arrays.toString(arr));
//        System.out.println(Arrays.toString(tree));

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int query = Integer.parseInt(st.nextToken());
            if(query == 1){
                int qStart = Integer.parseInt(st.nextToken());
                int qEnd = Integer.parseInt(st.nextToken());
                int value = Integer.parseInt(st.nextToken());
                update(1, 1, N, qStart, qEnd, value);
            }else if(query == 2){
                int qIndex = Integer.parseInt(st.nextToken());
                result = 0;
                getInfo(1, 1, N, qIndex);
                sb.append(result).append('\n');
            }
//            System.out.println(Arrays.toString(tree));
        }

        System.out.println(sb.toString());
    }
}
