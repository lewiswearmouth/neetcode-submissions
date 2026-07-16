class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        n = len(matrix[0])

        # determine if mid is less or greater than last integer of each row

        # matrix[mid][-1]

            # then determine in that row mid of it accoridng to n

        left_r, right_r = 0, m - 1

        while left_r <= right_r:

            mid_r = (left_r + right_r)//2

            if(matrix[mid_r][0] == target or matrix[mid_r][-1] == target):

                return True

            elif(matrix[mid_r][-1] > target and matrix[mid_r][0] < target):

                # now do binary search within this row

                left_c, right_c = 0, n - 1

                while(left_c <= right_c):

                    mid_c = (left_c + right_c)//2

                    if(matrix[mid_r][mid_c] == target):

                        return True

                    elif(matrix[mid_r][mid_c] > target):

                        right_c = mid_c - 1

                    else:

                        left_c = mid_c + 1

               

                return False

 

            elif (matrix[mid_r][-1] > target):

                right_r = mid_r - 1

            else:

                left_r = mid_r + 1

           

        return False