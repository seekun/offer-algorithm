class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count = count + 1
        return count


s = Solution()
print(s.numJewelsInStones("zZ", "ZZz"))