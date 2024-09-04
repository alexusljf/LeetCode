class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = 2**31 -1
        int_min = -1 * 2**31
        returnInt = 0
        sign = 1 #default to positive
        s = s.lstrip() # strip leading whitespace
        i = 0
        
        if i < len(s) and s[i] == '+':
            sign = 1
            i+=1
        elif i < len(s) and s[i] == '-':
            sign = -1
            i+=1
        
        for j in range(i,len(s)):
            if not s[j].isdigit():
                break
            print(f'current rturn int: {returnInt}, current char is {s[j]}')
            returnInt = returnInt * 10 + int(s[j])
            # handle rounding
            if sign * returnInt >= int_max:
                return int_max
            if sign * returnInt <= int_min:
                return int_min
            
        return sign * returnInt