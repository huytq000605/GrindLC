class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        result = 0
        n = len(energy)
        cur_en, cur_ex = initialEnergy, initialExperience
        for i in range(n):
            en, ex = energy[i], experience[i]
            if cur_en <= en:
                result += en + 1 - cur_en
                cur_en = en + 1
            if cur_ex <= ex:
                result += ex + 1 - cur_ex
                cur_ex = ex + 1
            cur_en -= en
            cur_ex += ex
        return result
