class Solution:
    def wordPattern(self, pattern: str, values: str) -> bool:
        mapping = {}
        prev = set()
        
        values = values.split(" ")
        if len(values) != len(pattern):
            return False
        
        for p, v in zip(pattern, values):
            if v not in prev and p not in mapping:
                prev.add(v)
                mapping[p] = v
            elif p not in mapping:
                return False
            elif v not in prev:
                return False
            else:
                if v != mapping[p]:
                    return False
        return True
