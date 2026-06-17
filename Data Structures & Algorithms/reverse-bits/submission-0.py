class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = f'{n:32b}'.replace(' ', '0')
        reversedInt = 0
        for i in range(32):
            cur_num = int(binary_string[i])
            reversedInt += cur_num*(2**i)

        return reversedInt