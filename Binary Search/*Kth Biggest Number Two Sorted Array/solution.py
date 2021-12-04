class Solution:
	def kth(self, arr1, arr2, k):
		if k > len(arr1) + len(arr2):
			return -1
		n1 = len(arr1)
		n2 = len(arr2)
		def dfs(s1, s2, k):
			if s1 >= n1:
				return arr2[s2 + k - 1]
			if s2 >= n2:
				return arr1[s1 + k - 1]
			if k == 1:
				if arr1[s1] > arr2[s2]:
					return arr1[s1]
				else:
					return arr2[s2]
			half = min(n1 - s1, n2 - s2, k // 2)
			if arr1[s1 + half - 1] > arr2[s2 + half - 1]:
				return dfs(s1 + half, s2, k - half)
			else:
				return dfs(s1, s2 + half, k - half)
		return dfs(0, 0, k)