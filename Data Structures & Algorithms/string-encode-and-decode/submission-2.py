class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for i in strs:
            l = len(i)
            temp.append(str(l) + '#' + i)
        temp = ''.join(temp)
        return temp

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1

            decoded.append(s[j:j + length])

            i = j + length
        return decoded

