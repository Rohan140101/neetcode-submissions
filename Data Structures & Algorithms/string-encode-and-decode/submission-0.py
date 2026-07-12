class Solution:

    def encode(self, strs: List[str]) -> str:
        # ans = ""
        # for s in strs:
        #     for i in range(len(s)):
        #         ans += f"{ord(s[i])}"
        #         ans += "256"
        #     ans += "257"
        # return ans

        ans = []
        for s in strs:
            ans.append(str(len(s)))
            ans.append("#")
            ans.append(s)

        return ''.join(ans)


    def decode(self, s: str) -> List[str]:
        answer = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            string = s[i:j]
            answer.append(string)
            i = j
        return answer

