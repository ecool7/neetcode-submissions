class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for i in strs:
            key = sorted(i)
            key = "".join(key)
            if key in dict:
                dict[key].append(i)
            else:
                dict[key] = [i]

        a = []

        for value in dict.values():
            a.append(value)
        return a

        