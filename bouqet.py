#
# Complete the 'flowerBouquets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER p
# 2. INTEGER q
# 3. STRING s
#

# import bisect

from bouqet_tests import t1,t2,t3,t4,t5 


# class WeightedIntervalScheduling(object):
#     def __init__(self, I):
#         self.I = sorted(I, key=lambda tup: tup[1])  # (key = lambda tup : tup[1])
#         self.OPT = []
#         self.solution = []

#     def previous_intervals(self):
#         start = [task[0] for task in self.I]
#         finish = [task[1] for task in self.I]
#         p = []

#         for i in range(len(self.I)):
#             # finds idx for which to input start[i] in finish times to still be sorted
#             idx = bisect.bisect(finish, start[i]) - 1
#             p.append(idx)

#         # print(p)
#         return p

#     def find_solution(self, j):
#         if j == -1:
#             return

#         else:
#             if (self.I[j][2] + self.compute_opt(self.p[j])) > self.compute_opt(j - 1):
#                 self.solution.append(self.I[j])
#                 self.find_solution(self.p[j])

#             else:
#                 self.find_solution(j - 1)

#     def compute_opt(self, j):
#         if j == -1:
#             return 0

#         elif (0 <= j) and (j < len(self.OPT)):
#             return self.OPT[j]

#         else:
#             return max(
#                 self.I[j][2] + self.compute_opt(self.p[j]), self.compute_opt(j - 1)
#             )

#     def weighted_interval(self):
#         if len(self.I) == 0:
#             return 0, self.solution

#         self.p = self.previous_intervals()

#         for j in range(len(self.I)):
#             opt_j = self.compute_opt(j)
#             self.OPT.append(opt_j)

#         self.find_solution(len(self.I) - 1)

#         print(self.OPT)
#         return self.OPT[-1], self.solution[::-1]


# def flowerBouquets(p, q, s):
#     if len(s) <= 1:
#         return 0
#     jobs = []
#     type1 = "000"

#     for i in range(len(s)):
#         if s[i:i + 3] == type1:
#             jobs.append((i, i + 3, p))
#         else:
#             cur = s[i: i + 2]
#             if cur == "01" or cur == "10":
#                 jobs.append((i, i + 2, q))
#     if not jobs:
#         return 0
#     # return findMaxProfit(jobs)
#     weightedinterval = WeightedIntervalScheduling(jobs)
#     max_weight, best_intervals = weightedinterval.weighted_interval()
#     # print(max_weight, best_intervals)
#     return max_weight


def findMaxProfit(jobs):
    tabulation = []
    for i in range(len(jobs)):
        tabulation.append(jobs[i][2])
    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            if jobs[i][1] < jobs[j][0]:
                tabulation[j] = max(tabulation[j], jobs[j][2] + tabulation[i])
    return tabulation[-1]


def flowerBouquets(p, q, s):
    if len(s) <= 1:
        return 0
    jobs = []
    type1 = '000'
    for i in range(len(s)):
        if s[i:i + 3] == type1:
            jobs.append([i, i + 2, p])
        else:
            cur = s[i: i + 2]
            if cur == '01' or cur == '10':
                jobs.append([i, i + 1, q])
    if not jobs:
        return 0
    print(findMaxProfit(jobs)) 




# print(t1)
flowerBouquets(t1[0],t1[1],t1[2])
