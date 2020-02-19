//https://leetcode.com/problems/k-closest-points-to-origin
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]>pq = new PriorityQueue<>((x,y) -> 
        {
            return Double.compare(Math.sqrt(x[0]*x[0] + x[1]*x[1]),Math.sqrt(y[0]*y[0]+y[1]*y[1]));
        }
                                                    );
        for (int[] x : points)
        {
        	pq.add(x);
        }
        
        int[][]res = new int[K][2];
        int i = 0;
        while (K != 0)
        {
        	res[i++] = pq.poll();
        	K--;
        }
        return res;
    }
}