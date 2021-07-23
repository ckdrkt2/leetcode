class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(map(int,list(str(num))))
        return num
# math solution
# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num%9==0 and num!=0:
#             return 9
#         else:
#             return num%9