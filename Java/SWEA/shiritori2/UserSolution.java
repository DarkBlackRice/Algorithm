package shiritori2;


import java.util.*;

class UserSolution {

    int N, M, roundCount;
    List<Integer> players;
    PriorityQueue<String>[] first = new PriorityQueue[26];
    List<String> store;
    TreeSet<String> wordLog;
    String word;

    public void init(int N, int M, char[][] mWords)
    {
        roundCount = 0;
        wordLog = new TreeSet<>();
        this.N = N;
        this.M = M;


        for(int i = 0; i<26; i++){
            first[i] = new PriorityQueue<>();
        }

        players = new LinkedList<>();
        for(int i = 1; i<=N; i++){
            players.add(i);
        }

        for(int i = 0; i<M; i++){
            word = String.valueOf(mWords[i]).trim();
            first[mWords[i][0] - 'a'].offer(word);
            wordLog.add(word);
        }
    }

    public int playRound(int mID, char mCh)
    {
        store = new ArrayList<>();
        StringBuilder sb;

        int cnt = 0;
        int now = mCh-'a';

        while(!first[now].isEmpty()){
            cnt++;
            word = first[now].poll();
            store.add(word);
            now = word.charAt(word.length()-1) - 'a';
        }

        for(String word : store){
            sb = new StringBuilder(word);
            word = sb.reverse().toString();
            if(wordLog.add(word)){
                first[word.charAt(0) - 'a'].offer(word);
            }
        }

        int firstPlayerIndex = players.indexOf(mID);
        Integer loser = players.get((firstPlayerIndex + cnt) % (N - roundCount++));
        players.remove(loser);

        return loser;
    }
}