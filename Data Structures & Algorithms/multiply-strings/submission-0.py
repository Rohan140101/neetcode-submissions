class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        def get_integer(num: str):
            numInt = 0
            for n in num:
                numInt = numInt*10 + (ord(n) - 48)
            return numInt

        num1int = get_integer(num1)
        num2int = get_integer(num2)
        return str(num1int * num2int)

        


        