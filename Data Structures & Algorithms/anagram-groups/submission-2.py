class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """seen = {}
        pointer = 0
        res = []
        for string in strs:
            s = str(sorted(string))
            if s in seen:
                res[seen[s]].append(string)
            else:
                seen[s] = pointer
                res.append([string])
                pointer += 1
        return res"""
        counts = defaultdict(list)
        for string in strs:
            curr_count = [0] * 26
            for char in string:
                curr_count[ord(char)-97] += 1
            counts[str(curr_count)].append(string)
        return list(counts.values())