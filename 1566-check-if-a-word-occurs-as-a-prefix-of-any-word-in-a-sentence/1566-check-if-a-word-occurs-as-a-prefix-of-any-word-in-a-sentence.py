class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        searchWordlen = len(searchWord)
        for i in range(len(words)):
            if searchWord == (words[i])[:searchWordlen]:
                return i+1
        return -1