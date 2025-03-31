class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def substrings(string):
            return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

        s_sub, t_sub = substrings(s), substrings(t)
        s_sub.append('')
        t_sub.append('')
        max_pal = 0

        
        for sub1 in s_sub:
            for sub2 in t_sub:
                contenate_sub = (sub1+sub2)
                if contenate_sub == contenate_sub[::-1]:
                    max_pal = max(max_pal, len(contenate_sub))
        
        return max_pal