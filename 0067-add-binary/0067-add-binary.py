class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        lenA = len(a)
        lenB = len(b)
        returnStr=[]
        while lenA > 0 or lenB > 0 or carry:
            sum = (int(a[lenA-1]) if lenA > 0 else 0) + (int(b[lenB-1]) if lenB > 0 else 0) + carry
            digit = sum % 2
            carry = sum // 2
            returnStr.append(str(digit))
            lenA -= 1
            lenB -= 1
        return (''.join(returnStr))[::-1]