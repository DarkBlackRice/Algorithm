package islandProtect;

import java.util.*;

class UserSolution
{   
    public int[][] initMap, modifiedMap;
    public int n, hash, reverseHash;

    public class Candidate {
        int r, c;
        boolean isVertical, isReverse;

        public Candidate(int r, int c, boolean isVertical, boolean isReverse){
            this.r = r;
            this.c = c;
            this.isVertical = isVertical;
            this.isReverse = isReverse;
        }
    }

    public ArrayList<Candidate> candidates[] = new ArrayList[10000];

	public void init(int N, int mMap[][])
	{
        // �� ũ�� �ޱ�
        n = N;
        // �� �ʱ�ȭ
        initMap = new int[n+2][n+2];
        modifiedMap = new int[n+2][n+2];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                initMap[i+1][j+1] = modifiedMap[i+1][j+1] = mMap[i][j];
            }
        }

        // ���� ���� ����� �ʱ�ȭ
        for(int i=0; i<10000; i++){
            candidates[i] = new ArrayList<Candidate>();
        }

        // ���� �ޱ�
        for(int m=2; m<=5; m++){

            // ����
            for(int r=1; r<=n-(m-1); r++){
                for(int c=1; c<=n; c++){
                    hash = 0;
                    for(int i=0; i<m-1; i++){
                        hash = hash * 10 + (initMap[r+i][c] - initMap[r+i+1][c] + 5);
                    }
                    candidates[hash].add(new Candidate(r, c, true, false));
                    // �Ųٷ�
                    reverseHash = 0;
                    for(int i=m-1; i>0; i--){
                        reverseHash = reverseHash * 10 + (initMap[r+i][c] - initMap[r+i-1][c] + 5);
                    }
                    if(hash != reverseHash){
                        candidates[reverseHash].add(new Candidate(r, c, true, true));
                    }
                }
            }

            // ����
            for(int c=1; c<=n-(m-1); c++){
                for(int r=1; r<=n; r++){
                    hash = 0;
                    for(int i=0; i<m-1; i++){
                        hash = hash * 10 + (initMap[r][c+i] - initMap[r][c+i+1] + 5);
                    }
                    candidates[hash].add(new Candidate(r, c, false, false));
                    // �Ųٷ�
                    reverseHash = 0;
                    for(int i=m-1; i>0; i--){
                        reverseHash = reverseHash * 10 + (initMap[r][c+i] - initMap[r][c+i-1] + 5);
                    }
                    if(hash != reverseHash){
                        candidates[reverseHash].add(new Candidate(r, c, false, true));
                    }
                }
            }   
        }
	}

	public int numberOfCandidate(int M, int mStructure[])
	{   
        if(M == 1) return n*n;

        hash = 0;
        for(int i=0; i<M-1; i++){
            hash = hash * 10 + (mStructure[i+1] - mStructure[i] + 5);
        }
		return candidates[hash].size();
	}

    public int bfs(int seaLevel){

        boolean vst[][] = new boolean[n+2][n+2];
        int dr[] = new int[] {0,1,0,-1},
            dc[] = new int[] {1,0,-1,0};

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[] {0, 0});
        int now[], next[];
        while(!q.isEmpty()){
            now = q.poll();
            for(int i=0; i<4; i++){
                next = new int[] {now[0] + dr[i], now[1] + dc[i]};
                if( 0<=next[0] && next[0]<n+2 && 0<=next[1] && next[1]<n+2 
                    && !vst[next[0]][next[1]] && modifiedMap[next[0]][next[1]] < seaLevel ){
                        vst[next[0]][next[1]] = true;
                        q.offer(next);
                    }
            }
        }

        int result = 0;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=n; j++){
                if(!vst[i][j]) result++;
            }
        }

        return result;
    }

	public int maxArea(int M, int mStructure[], int mSeaLevel)
	{   
        int result = -1;
        int height, row, col;

		if(M == 1) {
            for(int r=1; r<=n; r++){
                for(int c=1; c<=n; c++){
                    modifiedMap[r][c] = initMap[r][c] + mStructure[0];
                    result = Math.max(result, bfs(mSeaLevel));
                    modifiedMap[r][c] = initMap[r][c];
                }
            }
		}else{
            hash = 0;
            for(int i=0; i<M-1; i++){
                hash = hash * 10 + (mStructure[i+1] - mStructure[i] + 5);
            }
            if(candidates[hash].size()==0) {
				return result;
			}
            
            for(Candidate candidate : candidates[hash]){
                row = candidate.r;
                col = candidate.c;
                if(candidate.isVertical){
                    height = mStructure[0] + (candidate.isReverse? initMap[row + M-1][col] : initMap[row][col]);
                    for(int i=0; i<M; i++){
                        modifiedMap[row+i][col] = height;
                    }
                    result = Math.max(result, bfs(mSeaLevel));
                    for(int i=0; i<M; i++){
                        modifiedMap[row+i][col] = initMap[row+i][col];
                    }
                }else{
                    height = mStructure[0] + (candidate.isReverse? initMap[row][col + M-1] : initMap[row][col]);
                    for(int i=0; i<M; i++){
                        modifiedMap[row][col+i] = height;
                    }
                    result = Math.max(result, bfs(mSeaLevel));
                    for(int i=0; i<M; i++){
                        modifiedMap[row][col+i] = initMap[row][col+i];
                    }
                }
            }
        }
       
        return result;

	}
}
