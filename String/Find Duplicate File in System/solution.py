class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)
        for path in paths:
            elements = path.split()
            prefix_path = elements[0]
            for file in elements[1:]:
                file_name, content = file.split("(")
                content_to_path[content].append(f"{prefix_path}/{file_name}")
        return filter(lambda paths: len(paths) >= 2, content_to_path.values())
            
