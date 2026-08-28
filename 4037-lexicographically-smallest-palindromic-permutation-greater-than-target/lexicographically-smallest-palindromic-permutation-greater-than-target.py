class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        cnt = Counter(s)
        odd = ""

        for ch, freq in cnt.items():
            if freq % 2:
                if odd:
                    return ""
                odd = ch

        half_cnt = [0] * 26
        for ch in s:
            half_cnt[ord(ch) - ord('a')] += 1

        for i in range(26):
            half_cnt[i] //= 2

        m = len(s) // 2

        def make_palindrome(left):
            left = ''.join(left)
            return left + odd + left[::-1]

        left = []
        greater = False

        for i in range(m):
            t = ord(target[i]) - ord('a')

            if greater:
                for c in range(26):
                    if half_cnt[c] > 0:
                        left.append(chr(c + ord('a')))
                        half_cnt[c] -= 1
                        break
            else:
                if half_cnt[t] > 0:
                    left.append(target[i])
                    half_cnt[t] -= 1
                else:
                    found = False
                    for c in range(t + 1, 26):
                        if half_cnt[c] > 0:
                            left.append(chr(c + ord('a')))
                            half_cnt[c] -= 1
                            greater = True
                            found = True
                            break

                    if not found:
                        break

        candidate = make_palindrome(left) if len(left) == m else ""

        if candidate and candidate > target:
            return candidate

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
            pass

        for i in range(len(prefix), -1, -1):
            if i < len(prefix):
                removed = prefix.pop()
                half_cnt[removed] += 1

            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if half_cnt[c] > 0:
                    result = prefix + [c]
                    half_cnt[c] -= 1

                    for x in range(26):
                        result.extend([x] * half_cnt[x])

                    left_str = ''.join(chr(x + ord('a')) for x in result)
                    ans = left_str + odd + left_str[::-1]

                    return ans if ans > target else ""

        return ""