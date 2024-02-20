# testcase 1
timeSeries, duration = [1, 4], 3  # 6

# testcase 2
# timeSeries, duration = [1, 2], 2  # 3

# 아래에 코드를 작성해주세요.



# attack_time = []
# for i in range(duration):
#     for j in range(len(timeSeries)):
#         attack_time.append(timeSeries[j]+i)
#
# print(len(set(attack_time)))

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        attack_time = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i + 1] - timeSeries[i] > duration:
                attack_time += duration
            else:
                attack_time += timeSeries[i + 1] - timeSeries[i]
        return attack_time + duration