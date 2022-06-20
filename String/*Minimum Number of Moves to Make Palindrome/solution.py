class Solution:
	def minMovesToMakePalindrome(self, s: str) -> int:
		s = list(s)
		n = len(s)
		result = 0
		left = 0
		while left < n // 2:
			right = n - left - 1

			while left < right:
					if s[left] == s[right]:
							break
					else:
							right -= 1

			# s[left] will be in s[n//2]
			# We must move one by one, assume case "wggtt"
			# If we move w to middle, then we will have another character move w to different position
			if left == right:
				s[left], s[left + 1] = s[left + 1], s[left]
				
			else:
				for j in range(right, n - left - 1):
						(s[j], s[j + 1]) = (s[j + 1], s[j])
						result += 1
				left += 1
		return result