class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        st = []
        seen = set()

        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while st and st[-1] > ch and last[st[-1]] > i:
                seen.remove(st.pop())

            st.append(ch)
            seen.add(ch)

        return "".join(st)
