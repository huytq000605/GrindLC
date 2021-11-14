``` python
 @lru_cache(None)
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left + 1, right - 1)
```