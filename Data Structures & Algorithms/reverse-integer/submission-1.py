class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = 0
        maxLimit = 2**31-1
        minLimit = -2**31
        if x < 0:
            pos_x = -1 * x
            multiplier = -1
        else:
            pos_x = x
            multiplier = 1
        while pos_x:
            unit_place = pos_x%10
            pos_x = pos_x//10

            if (reverse_x*multiplier == maxLimit // 10 and pos_x > maxLimit % 10) or reverse_x*multiplier > maxLimit // 10:
                return 0

            if (reverse_x*multiplier == minLimit // 10 and pos_x < minLimit % 10) or reverse_x*multiplier < minLimit // 10:
                return 0 

            # if reverse_x > minLimit 
            reverse_x = reverse_x*10 + unit_place
        
        return reverse_x*multiplier