public int strStr(String haystack, String needle) {
    // base cases
    if (needle.length() == 0) {
        return 0;
    }
    if (haystack.length() == 0) {
        return -1;
    }

    for (int firstIndex = 0; firstIndex < haystack.length(); firstIndex++) {
        if (firstIndex + needle.length() > haystack.length()) { // checks if enough space
            break;
        }
        for (int j = 0; j < needle.length(); j++) { // uses j as offset, don't need to create new variable
            if (haystack.charAt(firstIndex + j) != needle.charAt(j)) {
                break;
            }
            if (j == needle.length() - 1) {
                return firstIndex;
            }
        }
    }
    return -1; // return -1 if not found
}