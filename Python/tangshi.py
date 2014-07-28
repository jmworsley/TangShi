#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys

mydict = { }

f = open("../Data/TangRhymesMap.csv")

for line in f:
  line = line.rstrip()
  rhyme, char = line.split(",")
  #key = str(char)
  #value = str(rhyme)
  key = char.decode("utf-8")
  value = rhyme.decode("utf-8")
  mydict[key] = value

f = open("../Data/SamplePoem.txt")
for line in f:
  line = line.rstrip()
  for key in line.decode("utf-8"):
    print key + " = " + mydict[key] + '\n'

