class Solution {
    public int maximumSwap(int num) {
        char[] numArray = Integer.toString(num).toCharArray();
        char[] tempArray = new char[numArray.length];
        int max = num;
        char tempChar;
        for (int i = 0; i < numArray.length; i++) {
            for (int j = 0; j < numArray.length; j++) {
                System.arraycopy(numArray, 0, tempArray, 0, numArray.length);
                //System.out.println("temp string: " + new String(tempArray) + ", i:" + i + ", j: " + j);
                if (i == j) {
                    continue;
                }
                tempChar = tempArray[i];
                tempArray[i] = tempArray[j];
                tempArray[j] = tempChar;
                //System.out.println("After swap: " + new String(tempArray));
                if (Integer.parseInt(new String(tempArray)) > max) {
                    max = Integer.parseInt(new String(tempArray));
                }
            }
        }
        return max;
    }
}