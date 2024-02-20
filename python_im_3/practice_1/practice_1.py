# testcase 1
# words, pref = ["pay","attention","practice","attend"], "at"  # 2

# testcase 2
words, pref = ["leetcode","win","loops","success"], "code"  # 0

# 아래에 코드를 작성해주세요.

# print(words[1].startswith("at"))

count = 0
for idx in range(len(words)):
    if words[idx].startswith(pref):
        count += 1

print(count)