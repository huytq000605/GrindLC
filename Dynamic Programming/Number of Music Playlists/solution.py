class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        N = n
        @cache
        def dfs(n, g):
            if g == 0:
                if n == g:
                    return 1
                return 0
            choose_new_song = n * dfs(n-1, g-1)
						# Choosing from N-n songs (have been in playlist)
						# Cannot repeat in k so N-n-k
            choose_old_song = max(0, N-n-k) * dfs(n, g-1)
            return (choose_new_song + choose_old_song) % (10**9 + 7)
        return dfs(n, goal)
            