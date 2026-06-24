class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # min = 0
        # for i in strs:
        #     l = len(i)
        #     if min > l:
        #         min=l

        prefix = ""
        for j in range(1, len(strs[0])+1):
            for i in range(len(strs)):
                if strs[0][:j] == strs[i][:j]:
                    print("Matched:", i,j, strs[0][:j])
                else:
                    print("Exit:", i,j, strs[0][:j] , strs[i][:j])
                    return prefix
            prefix = strs[0][:j]
        return prefix