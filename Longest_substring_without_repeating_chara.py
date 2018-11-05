class LongestSubStringWithoutRepeating:
    def lengthOfLongestSubstring(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        # if not s:
        #     return 0
        # start = 0
        # record = 0
        # end = 0
        # for end in range(len(s)):
        #     current_s = s[end]
        #     for j in range(start, end):
        #         if s[j] == current_s:
        #             record = max(end - start, record)
        #             start = j + 1
        # record = max(end + 1 - start, record)
        # return record

        # ---------------------------------
        # method 2: use dictionary
        last_seen = {}
        record = 0
        start = 0
        i = 0
        if not s:
            return 0
        for i, char in enumerate(s):
            if char in last_seen and start <= last_seen[char]:
                record = max(record, i - start)
                start = last_seen[char] + 1
            last_seen[char] = i
        record = max(record, i + 1 - start)
        return record


a = LongestSubStringWithoutRepeating()
print(a.lengthOfLongestSubstring(" "))
