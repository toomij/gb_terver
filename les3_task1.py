# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean):

import numpy as np
from math import factorial as fl

def combinations(k, n):
    return fl(n) / (fl(k) * fl(n - k))

salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
salaries_mean = salaries.sum() / salaries.size

print((np.sum((salaries - salaries_mean)**2) / salaries.size)**0.5)
print(np.sum((salaries - salaries_mean)**2) / salaries.size)
print(np.sum((salaries - salaries_mean)**2) / (salaries.size - 1))
