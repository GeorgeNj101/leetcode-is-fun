class Solution:
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l = 0
        result = 0
        for char in s:
            while char in st:
                st.remove(s[l])
                l+=1
            st.add(char)
            result = max(result, len(st))
        return result

    def main(self):
        s = "abcabcde"
        print(self.lengthOfLongestSubstring(s))
    
Solution().main()