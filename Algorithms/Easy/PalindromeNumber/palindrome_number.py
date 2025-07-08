class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        new_str = ''
        for char in range(1, len(x_str) + 1):
            new_str = new_str + x_str[-char]
        if x_str == new_str:
            return True
        return False
    
#63 I need to improve, its the first try