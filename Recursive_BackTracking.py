
# the video link : https://youtu.be/L0NxT2i-LOY?si=i1MLnY6BD7ApuVKl

# decisions -> recursion -> Base Case -> undo desision
#______________ this method is for <exhustive research>, when you want to see all solutions_________

class Solution:

    def substes(self, nums:list[int]) -> list[list[int]]:
        n = len(nums)
        result, current = [], []

        def backtrack(i):
            if i == n:
                result.append(current[:])
                return 
            
            #Don't pick it
            backtrack(i +1)

            #pick numbers
            current.append(nums[i])
            backtrack(i +1)
            current.pop()

        backtrack(0) 
        return result 


numbers = [1, 2, 3, 4]
solver = Solution()
all = solver.substes(numbers)
print(all)