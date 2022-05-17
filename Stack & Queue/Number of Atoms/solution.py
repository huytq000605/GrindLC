class Solution:
    def countOfAtoms(self, formula: str) -> str:
        atoms = [defaultdict(int)]
        i, n = 0, len(formula)
        current = ""
        count = 0
        
        def append_atom():
            nonlocal count, current
            if current:
                if count == 0:
                    count = 1
                atoms[-1][current] += count
                count = 0
                current = ""
        
        while i < n:
            l = formula[i]
            if l == "(":
                append_atom()
                atoms.append(defaultdict(int))
            elif l == ")":
                append_atom()
                i += 1
                count = 0
                while i < n and formula[i].isdigit():
                    count *= 10
                    count += int(formula[i])
                    i += 1
                if count == 0:
                    count = 1
                pop_atoms = atoms.pop()
                for key, value in pop_atoms.items():
                    atoms[-1][key] += value * count
                count = 0
                i -= 1
            elif l.isupper():
                append_atom()
                current = l
            elif l.islower():
                current += l
            elif l.isdigit():
                count *= 10
                count += int(l)
            i += 1
            
        append_atom()
        result = ""
        
        for key in sorted(atoms[0].keys()):
            result += key
            if atoms[0][key] > 1:
                result += str(atoms[0][key])
        return result