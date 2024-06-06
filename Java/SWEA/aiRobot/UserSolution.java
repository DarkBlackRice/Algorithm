package aiRobot;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.TreeMap;

class UserSolution
{
	final int MAX_WORK = 50000;
//	문제발견 ! : 기존의 로봇 iq를 기억하고 있어야 한다!
	class Robot {
		int hiatus, status, version;

		public Robot (int status, int version){
			this.hiatus = 0;
			this.status = status;
			this.version = version;
		}
	}

	class Work{
		int start, num;
		int[][] workingRobots;

		public Work(int start, int num){
			this.start = start;
			this.num = num;
			workingRobots = new int[num][2];
		}
	}

	Robot[] robots;
	TreeMap<Integer, PriorityQueue<Integer>> iq;
	Work[] works;

	public void init(int N)
	{
		robots = new Robot[N + 1];
		iq = new TreeMap<>();
		iq.put(0, new PriorityQueue<>());
		for (int i = 1; i <= N; i++) {
			robots[i] = new Robot(1, 1);
			iq.get(0).offer(i);
		}
		works = new Work[MAX_WORK];
	}

	public int callJob(int cTime, int wID, int mNum, int mOpt)
	{
		Work work = new Work(cTime, mNum);
		int cnt = 0;
		int res = 0;
		PriorityQueue<Integer> pq;
		while(cnt != mNum){
			int rID;

			if(mOpt == 0){
				pq = iq.firstEntry().getValue();
				while(pq.isEmpty()){
					iq.remove(iq.firstEntry().getKey());
					pq = iq.firstEntry().getValue();
				}
			}
			else{
				pq = iq.lastEntry().getValue();
				while(pq.isEmpty()){
					iq.remove(iq.lastEntry().getKey());
					pq = iq.lastEntry().getValue();
				}
			}
			rID = pq.poll();
			work.workingRobots[cnt][0] = rID;
			work.workingRobots[cnt++][1] = robots[rID].version;

			robots[rID].status = wID * -1;
			res += rID;
		}

		works[wID] = work;
//		System.out.println(Arrays.deepToString(work.workingRobots));
//		System.out.println(res);
		return res;
	}

	public void returnJob(int cTime, int wID)
	{
		Work work = works[wID];
		int rID, version;

		for (int i = 0; i < work.num; i++) {
			rID = work.workingRobots[i][0];
			version = work.workingRobots[i][1];

			if(robots[rID].status < 0 && robots[rID].version == version){
				robots[rID].hiatus += cTime - work.start;
				if(!iq.containsKey(robots[rID].hiatus)){
					iq.put(robots[rID].hiatus, new PriorityQueue<Integer>());
				}
				iq.get(robots[rID].hiatus).offer(rID);

				robots[rID].status = 1;
			}
		}
	}

	public void broken(int cTime, int rID)
	{
		if(robots[rID].status > 0) return;
		robots[rID].status = 0;
	}

	public void repair(int cTime, int rID)
	{
		if(robots[rID].status != 0) return;

		robots[rID].status = 1;
		robots[rID].hiatus = cTime;
		robots[rID].version += 1;

		if(!iq.containsKey(robots[rID].hiatus)){
			iq.put(robots[rID].hiatus, new PriorityQueue<Integer>());
		}
		iq.get(robots[rID].hiatus).offer(rID);
	}

	public int check(int cTime, int rID)
	{
		if(robots[rID].status > 0){
//			System.out.println(cTime - robots[rID].hiatus);
			return cTime - robots[rID].hiatus;
		}
//		System.out.println(robots[rID].status);
		return robots[rID].status;
	}
}