# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_begin = 0 #最大面积起点
        max_end = len(height)-1 #最大面积终点
        max_aera = min(height[0], height[-1]) * (max_end) #最大面积初值，头到尾
        begin = max_begin
        end = max_end
        while end > begin: #从两端向中间搜索
            #每次都头和尾中较小的一端向内搜索
            #从大的一端向内搜索可能会错过最大值
            #从小的一端不会，假设end端小，则仅有height[end-1]>height[end]时才可能出现新的最大值，
            #而不论height[begin+1]是否比height[begin]大，最大面积都不受影响
            #“决定木桶容量的是最短的那块板”
            if height[begin] > height[end]: 
                end = end -1
            else:
                begin = begin + 1
            aera = min(height[begin], height[end]) * (end - begin)
            if aera > max_aera:
                max_aera = aera
                max_begin = begin
                max_end = end

        return max_aera

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #O(n**2)的算法，全遍历比较
        max_aera = -1
        for i in range(len(height)):
            for j in range(len(height)):
                aera = min(height[i], height[j]) * abs(i-j)
                if aera > max_aera:
                    max_aera = aera
                    max_begin = i
                    max_end = j
        return max_aera

import random
l = [random.randint(1,100) for _ in range(100)]
print(l)
print(Solution().maxArea(l))
print(Solution().maxArea2(l))