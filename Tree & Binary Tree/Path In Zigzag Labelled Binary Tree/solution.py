class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        levelOfLabel = 1
        while (1 << levelOfLabel) - 1 < label:
            levelOfLabel += 1
            
        path = [label]
        while levelOfLabel > 1:
            start = 1 << (levelOfLabel - 1)
            end = (1 << levelOfLabel) - 1
    
            if levelOfLabel % 2 == 0:
                real_label = start + (end - label)
                label = real_label // 2
                path.append(label)
            else:
                fake_label = start + (end - label)
                label = fake_label // 2
                path.append(label)
                
            levelOfLabel -= 1
        return path[::-1]