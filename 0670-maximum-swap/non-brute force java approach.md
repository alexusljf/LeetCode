got this from ChatGPT, but also saw the same solution from LeetCode discussion boards.

As we can only make 1 swap, we should swap the earliest digit with the 1st largest digit that occurs
eg 2736 will return 7236, with 7 being the 1st largest that occurs (1st from 9 to 0)

public int maximumSwapGPT(int num) {
    char[] numArray = Integer.toString(num).toCharArray();
    int[] lastOccurrence = new int[10]; // Store the last occurrence of each digit.

    // Fill the last occurrence array.
    for (int i = 0; i < numArray.length; i++) {
        // - '0' to convert from char to int, eg '7' converted to int 7 in ASCII
        lastOccurrence[numArray[i] - '0'] = i;
    }

    // Iterate through the digits.
    for (int i = 0; i < numArray.length; i++) {
        // iterate from 9 to the current digit considering to swap, represented by numArray[i]
        for (int d = 9; d > numArray[i] - '0'; d--) {
            // Check if there's a larger digit to the right. (eg if we input 8271 and no digit is > 8 so we don't swap, 2nd pass will swap 2 with 7 to return 8721)
            // lastOccurence[d] is the last index that digit d occurs, if index of d is right of i, then swap it
            if (lastOccurrence[d] > i) {
                // Swap the digits.
                char temp = numArray[i];
                numArray[i] = numArray[lastOccurrence[d]];
                numArray[lastOccurrence[d]] = temp;

                // Convert the character array back to an integer and return it.
                return Integer.parseInt(new String(numArray));
            }
        }
    }

    // If no swap is made, return the original number.
    return num;
}