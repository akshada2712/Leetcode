class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.isScrambleHelper(s1, s2, memo)
        
    def isScrambleHelper(self, s1: str, s2: str, memo: Dict[Tuple[str, str], bool]) -> bool:
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            memo[(s1, s2)] = False
            return False

        if s1 == s2:
            memo[(s1, s2)] = True
            return True

        for i in range(1, len(s1)):
            if (self.isScrambleHelper(s1[:i], s2[:i], memo) and
                self.isScrambleHelper(s1[i:], s2[i:], memo)) or \
                (self.isScrambleHelper(s1[:i], s2[-i:], memo) and
                 self.isScrambleHelper(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True

        memo[(s1, s2)] = False
        return False