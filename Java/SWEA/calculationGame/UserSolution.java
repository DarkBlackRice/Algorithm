package calculationGame;

import java.util.*;

class UserSolution {
	
	final int MAX_CARDS = 50000;
	
	int cards[];
	int front, rear;
	LinkedList<Integer> calculated[][] = new LinkedList[20][20];
	int joker;
	
//	카드가 추가될 때 마다 계산 결과를 calculated 배열에 저장할 함수 선언
	void calculate(int index, boolean isFront) {
		int numOfJoker = 0;
		int sum = 0;
		int temp, result;
		
		for(int i=0; i<4; i++) {
			temp = cards[index+i];
			if(temp == -1) numOfJoker++;
			else sum += temp;
		}
		
		for(int i = 0; i < 20; i++) {
			result = (sum + (numOfJoker * i)) % 20;
			if(isFront) {
				calculated[i][result].addFirst(index);
			}else {
				calculated[i][result].addLast(index);
			}
			
		}
	}

    void init(int mJoker, int mNumbers[]) {
//    	전체 세팅 초기화
    	front = rear = MAX_CARDS;
    	cards = new int[MAX_CARDS*2 + 1];
    	for (int i = 0; i < 20; i++) {
    		for (int j = 0; j < 20; j++) {
				calculated[i][j] = new LinkedList<Integer>();
			}
		}
    	
//    	시작값 초기화
    	joker = mJoker % 20;
    	for(int i = 0; i<5; i++) {
    		cards[rear+i] = mNumbers[i];
    	}
    	for(int i = 0; i<2; i++) {
    		calculate(rear+i, false);
    	}
    }

    void putCards(int mDir, int mNumbers[]) {
    	boolean isFront = (mDir == 0);
    	if (isFront) {
    		front -= 5;
    		for(int i = 0; i < 5; i++) {
    			cards[front+i] = mNumbers[i];
    		}    		  		
    		for(int i = 4; i > -1; i--) {
    			calculate(front+i, true);
    		}
    		
    		
    	}else {
    		rear += 5;
    		for(int i = 0; i < 5; i++) {
    			cards[rear+i] = mNumbers[i];
    		}
    		int target = rear - 3;
    		for(int i = 0; i < 5; i++) {
    			calculate(target+i, false);
    		}
    	}
    }

    int findNumber(int mNum, int mNth, int ret[]) {
    	if(calculated[joker][mNum].size() >= mNth) {
    		int index;
    		index = calculated[joker][mNum].get(mNth-1);
    		for(int i = 0; i<4; i++) {
    			ret[i] = cards[index+i];
    		}
    		return 1;
    		
    	}
    	else {
    		return 0;
    	}
    }

    void changeJoker(int mValue) {
    	joker = mValue % 20;
    }
}