class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = str()
        for i in s:
            if i.isalnum():
                rev += i
        return rev.lower() == rev[::-1].lower()