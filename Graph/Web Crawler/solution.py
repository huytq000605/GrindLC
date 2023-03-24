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
        crawled = set([startUrl])
        def prefix(url):
            seen = 0
            for i, c in enumerate(url):
                if c == "/": seen += 1
                if seen == 3: return url[:i]
            return url
        
        start_prefix = prefix(startUrl)
        
        def dfs(url):
            nonlocal crawled, htmlParser
            for v in htmlParser.getUrls(url):
                if v in crawled: continue
                if prefix(v) != start_prefix: continue
                crawled.add(v)
                dfs(v)
        dfs(startUrl)
        return crawled
