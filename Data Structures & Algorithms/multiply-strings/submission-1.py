class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)
        if len(num2) > len(num1):
            return self.multiply(num2, num1)


        multiplication_ans = 0
        for i in range(m-1, -1, -1):
            unit_multiplicator = 10**(m-i-1)
            multiplicator = int(num2[i])
            carry = 0
            cur_multiplication_value = 0
            
            for j in range(n-1, -1, -1):
                multiplicand = int(num1[j])
                multiplied = carry + multiplicator*multiplicand
                carry = multiplied // 10
                cur_multiplication_value += (multiplied % 10)*10**(n-j-1)
            
            if carry > 0:
                cur_multiplication_value += carry*10**(n)

            multiplication_ans += unit_multiplicator * cur_multiplication_value

        return str(multiplication_ans)


        


        