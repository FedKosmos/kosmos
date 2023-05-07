#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random

print("Привет! Давай проверим знание таблицы умножения")
count_of_excersize = 10
count_correct_answers = 0

for i in range(1, count_of_excersize+1):
  a = random.randint(1,10)
  b = random.randint(1,10)
  print("Пример ", i, ". Сколько будет ", a, " * ", b)
  result = input()
  try:
    if (a * b) == int(result):
      print("Верно!")
      count_correct_answers += 1
    else:
      print("Провал... это будет ", a * b )
  except:
    print("введено что то не то")

print("Верных решений: ", count_correct_answers)
print("Ваша оценка: ", count_correct_answers / count_of_excersize * 5)

