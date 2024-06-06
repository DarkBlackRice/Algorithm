package listCopy;

import java.util.*;

class UserSolution
{	
	final int MAX_MAKE_LIST = 10;
    final int MAX_LENGTH = 200000;
    final int MAX_CHANGE = 110000;
	
	class Event{
		int prev, index, value;

		public Event(int prev, int index, int value) {
			super();
			this.prev = prev;
			this.index = index;
			this.value = value;
		}		
	}
	
	String makeString(char[] arr) {
		String res = "";
		
		for (int c = 0; arr[c] != 0; c++) {
			res += arr[c];
		}
//		System.out.println(res);
		return res;
	}
	
	int origin[][], lastEvent[], originNo, eventNo, addrNo;	
	Map<String, Integer> address;
	Event eventLog[];
	
	int curAddrNo;
	
	public void init()
	{
		origin = new int[MAX_MAKE_LIST][MAX_LENGTH];
		originNo = eventNo = addrNo = 0;
		address = new TreeMap<String, Integer>();
		lastEvent = new int[MAX_CHANGE];
		eventLog = new Event[MAX_CHANGE];
	}

	public void makeList(char mName[], int mLength, int mListValue[])
	{
//		���� �迭 ����
		System.arraycopy(mListValue, 0, origin[originNo], 0, mLength);
		
//		�迭 �̺�Ʈ �߰�
		eventLog[eventNo] = new Event(-1, originNo, -1); // �� prev == -1 �̸� ���� ������ ����Ʈ
		
//		�ش� �迭 �ּ� ����
//		System.out.print("���� ���� �迭 : ");
//		System.out.println(makeString(mName));
		address.put(makeString(mName), addrNo);
		
//		������ �̺�Ʈ ����
		lastEvent[addrNo] = eventNo;
		
//		��ȣ ������Ʈ
		originNo++;
		eventNo++;
		addrNo++;
	}

	public void copyList(char mDest[], char mSrc[], boolean mCopy)
	{
		if(mCopy) {
//			���� ������ ���,
//			mSrc �迭�� ������ �̺�Ʈ�� ���� �̺�Ʈ�� ������ �� �̺�Ʈ ���� �� �߰�
//			System.out.print("����Ÿ�� : ");
//			System.out.println(makeString(mSrc));
			int prev = lastEvent[address.get(makeString(mSrc))]; 
			eventLog[eventNo] = new Event(prev, -1, -1); // ��, index == -1 �̸� ���� ����� ����Ʈ
			address.put(makeString(mDest), addrNo);
//			System.out.print("���絥���� �̸� : ");
//			System.out.println(makeString(mDest));			
			lastEvent[addrNo] = eventNo;

//			��ȣ ������Ʈ
			eventNo++;
			addrNo++;
			
		}else {
//			���� ������ ���,
//			mSrc �迭�� ���� ������ �̺�Ʈ �ּҸ� �����ϵ��� address �ʿ� ������ �߰�
			address.put(makeString(mDest), address.get(makeString(mSrc)));
		}
	}

	public void updateElement(char mName[], int mIndex, int mValue)
	{
//		�ش� �迭�� �� �̺�Ʈ ���� �� ������ �̺�Ʈ ������Ʈ
//		System.out.println(makeString(mName));
//		System.out.println(address.get(makeString(mName)));
		int curAddrNo = address.get(makeString(mName));
		int prev = lastEvent[curAddrNo];
		eventLog[eventNo] = new Event(prev, mIndex, mValue);
		lastEvent[curAddrNo] = eventNo;		
		
//		��ȣ ������Ʈ
		eventNo++;
		
	}

	public int element(char mName[], int mIndex)
	{	
//		System.out.println(makeString(mName));
		int curAddrNo = address.get(makeString(mName));
		int curEventNo = lastEvent[curAddrNo];
		while (true){
			
			Event curEvent = eventLog[curEventNo];
			
			if(curEvent.prev == -1) {
				return origin[curEvent.index][mIndex];
			}else if(curEvent.index == mIndex){
				return curEvent.value;
			}
			
			curEventNo = curEvent.prev;
			
		}
	}
}

