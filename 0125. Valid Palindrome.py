# without regular expression
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         a = []
#         for i in range(len(s)):
#             if s[i].isalnum():
#                 a.append(s[i].lower())
#         if a == list(reversed(a)):
#             return True
#         else:
#             return False

# with regular expression
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        str1 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return str1 == str1[::-1]