class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def matches(word):
            p_to_w = {}
            w_to_p = {}

            for p, w in zip(pattern, word):
                if p in p_to_w:
                    if p_to_w[p] != w:
                        return False
                else:
                    if w in w_to_p:
                        return False
                    
                    p_to_w[p] = w
                    w_to_p[w] = p

            return True

        return [word for word in words if matches(word)]