class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        returnArray = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                returnArray.append("FizzBuzz")
            elif i%3==0:
                returnArray.append("Fizz")
            elif i%5==0:
                returnArray.append("Buzz")
            else:
                returnArray.append(str(i))
        return returnArray
            
        