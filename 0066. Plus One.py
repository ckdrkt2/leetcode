class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(map(str,digits))
        a = str(int(a)+1)
        a = list(map(int,list(a)))
        return a