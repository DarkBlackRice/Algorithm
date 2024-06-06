package soldierManage;

class UserSolution
{	
	static int score, maxId, version[], teamInfo[];
	static Node tempNode;
	static Team team[];
	
//	��� ��ü ���� : �� �ϴ��� + �������� ����������!
	public class Node{
		int ver, value;
		Node next;
		
		public Node(int value, Node next) {
			super();
			this.ver = ++version[value];
			this.value = value;
			this.next = next;
		}		
		
	}
	
//	�� ��ü ���� : head�� tail �迭 ���� 6��¥���� ���� �ϳ��� ������ ����
	public class Team{
		Node head[] = new Node[6];
		Node tail[] = new Node[6];
	}
	
	public void init()
	{
//		�ʱ�ȭ
//		1. �� �迭 ���� 6¥�� ����
//		2. �� ���� head �迭�� tail �迭�� ���� ���̳�� ����	
//		3. ���� �迭 (���� 10�� : id�� �ִ� 10�� ������) ����
//		4. ������ �迭 (") ����
		
		version = new int[100010];
		teamInfo = new int[100010];
		
		team = new Team[6];
		for (int i = 1; i < 6; i++) {
			team[i] = new Team();
			
			for (int j = 1; j < 6; j++) {
				team[i].tail[j] = team[i].head[j] = new Node(0, null);
			}
		}
		
	}
	
	public void hire(int mID, int mTeam, int mScore)
	{
//		1. mID ���� ������, ���� ������ ++�� ���� �������� ������  ��� ����
//		2. mTeam ��° �� �迭�� mSccore ��° tail�� ����Ű�� ��� �ڷ� ������
//			--> tail�� ����Ű�� ����� next ���� ������(null)���� 1.���� ������ ���� �ٲ��ְ�
//			--> tail�� 1.���� ������ ��带 ����Ű���� ������ָ� ��! �ų���~! 
		
		Node newNode = new Node(mID, null);
		team[mTeam].tail[mScore].next = newNode;
		team[mTeam].tail[mScore] = newNode;
		teamInfo[mID] = mTeam;
		
	}
	
	public void fire(int mID)
	{
//		����[mID] = -1
//		������ �����ϴ� ��쿡�� ������ ���� �� �����Ƿ� ����!
//		���� ����ϰ� �� �� ������ �����Ǹ� ������ 3�� ��
//		���� �ذ�Ǿ��ٰ� ����Ǿ� ���� ������ �� �� �� ����� ������ 3���� ���� �����Ͱ� �� �� �߻�
//		������ ������ ����Ǿ������Ƿ� ����� �� �ִ� ���!
		
//		������ ������ �ÿ���, ��뿩�θ� �Ǵ��� �� �ִ� �迭�� �ʿ��ϴ�!
		version[mID] = -1;
		
	}

	public void updateSoldier(int mID, int mScore)
	{
//		�ѹ� ��  ����� 
//		--> ���߿� ���迭�� ���� �� �� ������ ������ ������
//			: �������� �����͸� ó������ �ʰ� ���� �߰��Ѵ�! (lazy�ϰ� ó���Ѵ� ���� �𸣰ٳ�)
		
		hire(mID, teamInfo[mID], mScore);
	}

	public void updateTeam(int mTeam, int mChangeScore)
	{
//		���Ⱑ ���� ����� : �̰� ���۷��� �ڵ� ���鼭 ������ �����Ϸ�
//		��� �׷��� ������� �ʰ� ��� ����ٰ� ���Ͽ� ���̸� �Ǵµ�,
//		����ó���� �� ���� �����ϱ� �װŸ� �� �����غ���
		
		
			
		if(mChangeScore < 0) {
			
			for (int i = 2; i < 6; i++) {
				
//				�ش� ��&���� �����Ͱ� �����ϴ��� Ȯ������ ������ ������ �߻�!
//				��ȿ�� ������ �̵��� ���������� �ұ��ϰ� �����͸� �ű�� �õ��� �ϸ�
//				�̵��� ��� (��, score �ε�����) �� tail �����Ͱ� ���̰� �� (���̳�带 ����Ŵ)
//				����, null check�� ������ �ƴ� �ʼ�
				
				if(team[mTeam].head[i].next == null) continue;
				
				score = i + mChangeScore < 1? 1 : i + mChangeScore;
				
				team[mTeam].tail[score].next = team[mTeam].head[i].next;
				team[mTeam].tail[score] = team[mTeam].tail[i];
				
//				���� ���� �ʱ�ȭ �۾� : Ư�� head�� next�� nulló���ϴ� �κ� ��������!
				team[mTeam].tail[i] = team[mTeam].head[i];
				team[mTeam].head[i].next = null;
				
			}
			
		}else if(mChangeScore > 0) {
			
			for (int i = 4; i > 0; i--) {
				
				if(team[mTeam].head[i].next == null) continue;
				
				score = i + mChangeScore > 5 ? 5 : i + mChangeScore;
				
				team[mTeam].tail[score].next = team[mTeam].head[i].next;
				team[mTeam].tail[score] = team[mTeam].tail[i];
				
//				���� ���� �ʱ�ȭ �۾� : Ư�� head�� next�� nulló���ϴ� �κ� ��������!
				team[mTeam].tail[i] = team[mTeam].head[i];
				team[mTeam].head[i].next = null;
				
			}
		}
		
		
	}
	
	public int bestSoldier(int mTeam)
	{
//		�̰� �� �д°� lazy�� �װ�
//		���� head�迭�� 5�� ���� ���ʴ�� �о,
//		�迭�� ������ ������ ��ȸ�ϸ鼭 mID���� �ִ��� ã��
//		������ ���� head �ε�����!
//		: �� ������ ���� ���� ����(5��) ��Ϻ��� �� Ȯ���Ѵٴ� ��
//		����! ���� üũ ��������! �����迭�� mID �񱳸� �� �� ��!
		
		maxId = 0;
		
//		���� ������ ���� 5����  head���� ���캸��
		for (int i = 5; i > 0; i--) {
			
			tempNode = team[mTeam].head[i].next;
			
//			���� �ش� ������ �ش��ϴ� ���� ���ٸ� ���� ������ �Ѿ����
			if(tempNode == null) continue;
			
			while(tempNode != null) {
				
				if(tempNode.ver == version[tempNode.value]) {
					maxId = maxId < tempNode.value ? tempNode.value : maxId;
				}
				tempNode = tempNode.next;
				
			}
			
			if (maxId != 0) return maxId;
			
		}
		
		return 0;
	}
}