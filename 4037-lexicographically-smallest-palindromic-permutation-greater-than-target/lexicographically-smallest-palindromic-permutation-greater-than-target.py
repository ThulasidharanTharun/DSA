class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        odd = ""

        # A palindrome can have at most one odd-frequency character
        for ch, freq in cnt.items():
            if freq % 2:
                if odd:
                    return ""
                odd = ch

        # Character counts for the first half
        half_cnt = [0] * 26
        for ch in s:
            half_cnt[ord(ch) - ord('a')] += 1

        for i in range(26):
            half_cnt[i] //= 2

        m = len(s) // 2

        def make_palindrome(left):
            left = ''.join(left)
            return left + odd + left[::-1]

        # Greedily find the first position where we can become > target
        left = []
        greater = False

        for i in range(m):
            t = ord(target[i]) - ord('a')

            if greater:
                # Choose smallest available character
                for c in range(26):
                    if half_cnt[c] > 0:
                        left.append(chr(c + ord('a')))
                        half_cnt[c] -= 1
                        break
            else:
                # Try to match target[i]
                if half_cnt[t] > 0:
                    left.append(target[i])
                    half_cnt[t] -= 1
                else:
                    # Need to find a larger character
                    found = False
                    for c in range(t + 1, 26):
                        if half_cnt[c] > 0:
                            left.append(chr(c + ord('a')))
                            half_cnt[c] -= 1
                            greater = True
                            found = True
                            break

                    # No larger character here means we need backtracking
                    if not found:
                        break

        candidate = make_palindrome(left) if len(left) == m else ""

        # If direct greedy construction works
        if candidate and candidate > target:
            return candidate

        # Try changing one earlier position from right to left
        # Start again with full counts
        half_cnt = [0] * 26
        for ch in s:
            half_cnt[ord(ch) - ord('a')] += 1
        for i in range(26):
            half_cnt[i] //= 2

        prefix = []

        for i in range(m):
            c = ord(target[i]) - ord('a')
            if half_cnt[c] == 0:
                break
            prefix.append(c)
            half_cnt[c] -= 1
        else:
            # All first-half characters matched
            pass

        # Backtrack from right to left
        for i in range(len(prefix), -1, -1):
            if i < len(prefix):
                removed = prefix.pop()
                half_cnt[removed] += 1

            t = ord(target[i]) - ord('a')

            # Choose smallest available character greater than target[i]
            for c in range(t + 1, 26):
                if half_cnt[c] > 0:
                    result = prefix + [c]
                    half_cnt[c] -= 1

                    # Fill remaining with smallest characters
                    for x in range(26):
                        result.extend([x] * half_cnt[x])

                    left_str = ''.join(chr(x + ord('a')) for x in result)
                    ans = left_str + odd + left_str[::-1]

                    return ans if ans > target else ""

        return ""