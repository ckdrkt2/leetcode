class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if A[i] % 2 != 0:
                A.append(A[i])
                A[i] = -1
        for i in range(A.count(-1)):
            A.remove(-1)
        return A