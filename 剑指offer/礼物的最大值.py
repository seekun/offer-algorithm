class Solution:
    def getmaxValue(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0
        # 用于存放中间数值的临时数组
        temp = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                if i > 0:
                    up = temp[j]
                if j > 0:
                    left = temp[j - 1]
                # 左或者上的路径和 + 本节点的值， 尝试记忆大概思路。 从终点开始思考
                temp[j] = max(up, left) + values[i * rows + j]
        return temp[-1]


s = Solution()
a = s.getmaxValue([1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5], 4, 4)
print(a)

# 用动态规划求解
