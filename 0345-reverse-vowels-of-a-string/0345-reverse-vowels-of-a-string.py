class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        vowels = ['a','e','i','o','u']
        l, r = 0, len(sList)-1
        while l < r:
            while sList[l].lower() not in vowels and l<r:
                print(f'L skipping over {sList[l]}')
                l += 1
            while sList[r].lower() not in vowels and l<r:
                print(f'R skipping over {sList[r]}')
                r -= 1
            temp = sList[l]
            print(f'swapping L {l} and R {r}, sList[l]: {sList[l]}, sList[r]: {sList[r]}')
            sList[l] = sList[r]
            sList[r] = temp
            # update values after swapping value
            l+=1
            r-=1
        
        return ''.join(sList)

