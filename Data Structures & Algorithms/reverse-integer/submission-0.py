class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = 0
        if x < 0:
            pos_x = -1 * x
            multiplier = -1
        else:
            pos_x = x
            multiplier = 1
        while pos_x:
            unit_place = pos_x%10
            reverse_x = reverse_x*10 + unit_place
            pos_x = pos_x//10

        answer = reverse_x * multiplier
        if answer > 2**31 - 1 or answer < -2**31:
            return 0
        return reverse_x*multiplier