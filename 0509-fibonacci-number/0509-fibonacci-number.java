class Solution {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    
    public int fib(int n) {
        if(map.containsKey(n)){
            return map.get(n);
        }    
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }
        else{
            map.put(n,fib(n-1) + fib(n-2));
            return fib(n-1) + fib(n-2);
        }
    }
}