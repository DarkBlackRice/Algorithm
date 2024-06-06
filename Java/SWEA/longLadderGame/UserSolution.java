package longLadderGame;

import java.util.*;

class UserSolution
{   
    final int LAST = 1000000000;
    
    class Node{
        int x, y;
        Node prev, next;
        Node(Node prev, Node next, int x, int y){
            this.x = x;
            this.y = y;
            this.prev = prev;
            this.next = next;
        }
        Node(int x, int y){
            this(null, null, x, y);
        }
    }

    Node ladder[] = new Node[101];
    Node cL, cR, nL, nR, now;
    TreeMap<Integer, Node> nodeIndex[] = new TreeMap[101];

	public void init()
	{
        for(int i = 1; i < 101; i++){
            ladder[i] = new Node(i, 0);
            ladder[i].next = new Node(ladder[i], null, i, LAST);
            nodeIndex[i] = new TreeMap<Integer, Node>();
            nodeIndex[i].put(0, ladder[i]);
            nodeIndex[i].put(LAST, ladder[i].next);
        }
	}

	public void add(int mX, int mY)
	{   
        // ��� �����ϱ�
        cL = nodeIndex[mX].floorEntry(mY).getValue();
        cR = nodeIndex[mX+1].floorEntry(mY).getValue();
        nL = new Node(cR, cL.next, mX, mY);
        nR = new Node(cL, cR.next, mX+1, mY);
        // ����Ī ��Ʈ
        cL.next.prev = nL;
        cR.next.prev = nR;
        cL.next = nR;
        cR.next = nL;

        // �ε��� �߰��ϱ�
        nodeIndex[mX].put(mY, nL);
        nodeIndex[mX+1].put(mY, nR);
	}

	public void remove(int mX, int mY)
	{
        cL = nodeIndex[mX].get(mY);
        cR = nodeIndex[mX+1].get(mY);

        // Ÿ���� ���� ��带 ����Ī�Ͽ� ����
        cL.prev.next = cR.next;
        cR.prev.next = cL.next;
        // Ÿ���� ���� ��带 ����Ī�Ͽ� ����
        cL.next.prev = cR.prev;
        cR.next.prev = cL.prev;

        // �ε��� �����ϱ�
        nodeIndex[mX].remove(mY);
        nodeIndex[mX+1].remove(mY);
	}

	public int numberOfCross(int mID)
	{   
        now = ladder[mID].next;
        int cnt = 0;
        while(now.next != null){
            cnt++;
            now = now.next;
        }
//        System.out.println(cnt);
		return cnt;
	}

	public int participant(int mX, int mY)
	{
		now = nodeIndex[mX].floorEntry(mY).getValue();
//		System.out.println(now.x + " " + now.y);
        while(now.prev != null){
            now = now.prev;
        }
//        System.out.println(now.x + " " + now.y);
        return now.x;
	}
}