import csv
import math
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


with open("r1z1.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

def commonMeanFunc (data):
    sum = 0
    for i in data:
        sum += i
    return sum / volume


def findModa(nums, k):
    # Step 1: Create a dictionary (`mp`) to store the frequency of each element in the array.
    mp = {}
    # Step 2: Create buckets to store elements based on their frequency.
    buckets = [[] for i in range(len(nums) + 1)]

    # Step 3: Iterate through the array to populate the `mp` dictionary.
    for n in nums:
        mp[n] = 1 + mp.get(n, 0)

    # Step 4: Iterate through the items in `mp` and distribute elements into the corresponding buckets based on their frequency.
    for n, c in mp.items():
        buckets[c].append(n)

    # Step 5: Iterate through the buckets from right to left (highest to lowest frequency) and append elements to the answer list until the desired k elements are collected.
    ans = []
    for i in range(len(buckets) - 1, 0, -1):
        if len(buckets[i]) > 0:
            return [buckets[i], i]


def find_mediana(data):
    data.sort()
    return data[int(len(data) / 2)]


def calculate_quartiles(data):
    # Сортируем входные данные
    sorted_data = sorted(data)

    # Находим первый квартиль (Q1)
    q1_index = int((len(sorted_data) + 1) / 4)
    q1 = sorted_data[q1_index - 1]  # -1, так как индексы начинаются с 0

    # Находим третий квартиль (Q3)
    q3_index = int(3 * (len(sorted_data) + 1) / 4)
    q3 = sorted_data[q3_index - 1]  # -1, так как индексы начинаются с 0

    return q1, q3


def calculate_iqr(data, q1, q3):
    sorted_data = sorted(data)
    iqr = q3 - q1
    return iqr




data = [float(sublist[0]) for sublist in data_read[1:]] #parsing data
print(data)


volume = len(data)
print(f'Обьем выборки = {volume}')

minimum = min(data)
print(f'Минимальная варианта {minimum}')

maximum = max(data)
print(f'Максимальная варианта {maximum}')

print(f'Размах: {maximum - minimum}')

mean = commonMeanFunc(data)
print(f'Простая средняя выборки: {mean}')

dispersion = sum((item - mean)**2 for item in data) / volume
print(f'Дисперсия: {dispersion}')

deviation = math.sqrt(dispersion)
print(f'Стандартное отклонение {deviation}')

asymmetry_coefficient = (sum((item - mean) ** 3 for item in data) / volume )/ (deviation ** 3)
print(f'Коэффицент ассиметрии {asymmetry_coefficient}')

quartil_25, quartil_75 = calculate_quartiles(data)
print(f'Квартиль 25%: {quartil_25}')
print(f'Квартиль 75%: {quartil_75}')

intr_width = calculate_iqr(data, quartil_25, quartil_75)
print(f'Интерквантильная широта {intr_width}')

find_moda_result = findModa(data,4)
print(f'Мода (моды): {find_moda_result[0]}. Встречается(ются) {find_moda_result[1]} раз')
print(f'Медиана: {find_mediana(data)}')


print('\n')


data_frame = pd.read_csv("r1z1.csv")

print(f"Maximum: {data_frame.max()}")
print(f"Minimum: {data_frame.min()}")
print(f"Average: {data_frame.mean()}")
print(f"Unbiased variance: {data_frame.var()}")
print(f"Biased variance: {data_frame.var() * (len(data) - 1) / len(data)}")
print(f"Standard deviation: {data_frame.std()}")
print(f"Mode: {data_frame.mode()}")
print(f"Median: {data_frame.median()}")
print(f"25% Quantile: {data_frame.quantile(0.25)}")
print(f"75% Quantile: {data_frame.quantile(0.75)}")
print(f"Interquartile latitude: {data_frame.quantile(0.75) - data_frame.quantile(0.25)}")

# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# calculations = ['max', 'min', 'avg']
#
# ax.bar(calculations, np.random.rand(len(calculations)))