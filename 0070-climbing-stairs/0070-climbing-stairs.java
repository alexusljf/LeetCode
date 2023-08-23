class Solution {
    
    // create a hashmap to store the previously calculated number of steps
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    
    public int climbStairs(int n) {
        // if number of steps already belong in the map then return it
        if (map.containsKey(n)) {
            return map.get(n);
        }
        // base cases of 0,1,2
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        // else we calculate the number of steps (which is a Fibonacci) and put into the map, then return it 
        else {
            int steps = climbStairs(n - 1) + climbStairs(n - 2);
            map.put(n, steps);
            return steps;
        }
    }
}