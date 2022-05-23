class Solution:
    def isPalindrome(self, x: int) -> bool:
        divider = 1
        while x >= divider * 10:
            divider *= 10

        while x:
            left = x // divider
            right = x % 10
            if left != right:
                return False
            else:
                x = (x % divider) // 10
                divider //= 100
        return True