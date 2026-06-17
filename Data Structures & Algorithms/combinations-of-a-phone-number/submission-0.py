class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letterListForDigit = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        n = len(digits)
        if n == 0:
            return []
        letterCombos = []

        def getDigitCombination(i, string):
            # print(i, string)
            if i == n:
                letterCombos.append(string)
                return

            lettersOfDigit = letterListForDigit[digits[i]]
            for letter in lettersOfDigit:
                getDigitCombination(i+1, string + letter)

        getDigitCombination(0, "")
        return letterCombos
