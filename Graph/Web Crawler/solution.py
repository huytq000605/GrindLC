# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        result = set()
        def same_host(url1, url2):
            slash = 0
            if len(url1) > len(url2):
                url1, url2 = url2, url1
            for i in range(len(url2)):
                if slash == 3 or (i == len(url1) and url2[i] == '/'): break
                if url1[i] != url2[i]: return False
                if url1[i] == '/': slash += 1
            return True

        
        def dfs(u):
            for v in htmlParser.getUrls(u):
                if v in result or not same_host(u, v): continue
                result.add(v)
                dfs(v)
        result.add(startUrl)
        dfs(startUrl)
        return result

