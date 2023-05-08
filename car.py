#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time
import random
from colorama import init, Fore

car="""
                                                                                    .------.
                                                                                   /       |
                                                                               .--'        -----.
                                                                              / _    777     _  |
                                                                             |_/.\_________ /.\_|
                                                                               \_/          \_/
"""

car1 = car
car2 = car
car2 = car2.replace("777","981")
car3 = car
car3 = car3.replace("777 ","fish")
winner = 0
debug = 0

for i in range(1,200):

  os.system('cls||clear')
  
  if car1.find("\n|") > 0:
    car1 = car1 + "    " + "Green win!"
    winner = 1
  else:
    space1 = ' ' * random.randint(1,2)

  if car2.find("\n|") > 0:
    car2 = car2 + "    " + "Red win!"
    winner = 2
  else:
    space2 = ' ' * random.randint(1,2)

  if car3.find("\n|") > 0:
    car3 = car3 + "    " + "Yellow win!"
    winner = 3
  else:
    space3 = ' ' * random.randint(1,2)

  if car1.find("\n |") > 0 and len(space1) > 1:
    space1 = ' ';

  if car2.find("\n |") > 0 and len(space2) > 1:
    space2 = ' ';

  if car3.find("\n |") > 0 and len(space3) > 1:
    space3 = ' ';

  if winner == 0:
    car1=car1.replace('\n' + space1, '\n')
    car2=car2.replace('\n' + space2, '\n')
    car3=car3.replace('\n' + space3, '\n')

  print (Fore.GREEN + car1)
  print ("")
  print (Fore.RED + car2)
  print ("")
  print (Fore.YELLOW + car3)
  print ("")
  
  if debug == 1:
    print (Fore.WHITE + "Debug info. Position of |")
    print (str(car1.find("\n|")), " ")
    print (str(car2.find("\n|")), " ")
    print (str(car3.find("\n|")), " ")

  time.sleep(0.1)

  if winner > 0:
    break


