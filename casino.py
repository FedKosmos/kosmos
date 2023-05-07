#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time
import random
from colorama import init, Fore

while True:
  a = random.randint(1,9)
  b = random.randint(1,9)
  c = random.randint(1,9)

  print (a, " ", b, " ", c, end = "\r")
  time.sleep(0.1)

  if a == b and b == c:
    print (a, " ", b, " ", c)
    print ("Вы победили!")
    break
  elif a == b or b == c or a == c:
    print (a, " ", b, " ", c)
    print ("2 из 3! Попробуйте ещё раз и будет бинго!")
    break

