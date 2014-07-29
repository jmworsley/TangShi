#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import codecs

ping = re.compile(u'.平')
shang = re.compile(u'上聲')
ru = re.compile(u'入')
qu = re.compile(u'去')

mydict = { }

# f = open("../Data/TangRhymesMap.csv")
f = codecs.open("../Data/TangRhymesMap.csv", "r", "utf-8")

for line in f:
  line = line.rstrip()
  value, key = line.split(",")
  #key = char.decode("utf-8")
  #value = rhyme.decode("utf-8")
  mydict[key] = value

f = codecs.open("../Data/SamplePoem.txt", "r", "utf-8")
for line in f:
  line = line.rstrip()
  for key in line:
    if key not in mydict:
      print key
    elif ping.match(mydict[key]):
      print key + " = " + " Ping"
    elif shang.match(mydict[key]):
      print key + " = " + " Shang"
    elif qu.match(mydict[key]):
      print key + " = " + " Qu"
    elif ru.match(mydict[key]):
      print key + " = " + " Ru"
    else:
      print key + " = " + " *"

