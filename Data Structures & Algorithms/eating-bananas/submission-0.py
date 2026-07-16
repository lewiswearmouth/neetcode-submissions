import math
# O(mlogn) time O(1) space
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #k is bananas per hour

        # x bananas, h hours

        # h * k >= x doesn't work bc must also consider piles

        # h * k is at least length of n

       

        # k can range from [1, maxVal]

        left, right = 1, max(piles)
        res = right

        while left <= right:

            k = (left+right)//2

            h_calc = 0

            for bananas in piles:

                h_calc += math.ceil(bananas/k)

           

            if h_calc <= h:

                res = min(res, k)

                right = k - 1

            else:

                left = k + 1

 

        return res

 

        # ex: [3, 1, 2, 3] h = 4 -> k = 3

       

        # ex: [3, 1, 2, 3] h = 8 -> k = 2

        # ex: [4, 1, 2, 3] h = 8 -> k = 2

        # ex: [5, 1, 2, 3] h = 8 -> k = 3

 

        # if h is greater than max val:

            #k = ceiling(h/max val)

 

        # ex2: [9, 10, 1, 3] h = 5 -> k = 9