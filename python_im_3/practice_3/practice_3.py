# testcase 1
names = ['Mary', 'John', 'Emma']
heights = [180,165,170]
# ["Mary","Emma","John"]

# testcase 2
# names = ["Alice", "Bob", "Bob"]
# heights = [155,185,150]
# ["Bob","Alice","Bob"]



# 아래에 코드를 작성해주세요.


sort_names = []
for i in range(len(heights)):
    a = heights.index(max(heights))
    sort_names.append(names[a])
    del heights[a]
    del names[a]


print(sort_names)

