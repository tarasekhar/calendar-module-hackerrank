#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:19:33 2019

@author: starsekhar
"""
import calendar

index={0:"MONDAY", 1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}

day=input().split()
month=int(day[0])
date=int(day[1])
year=int(day[2])

x=int(calendar.weekday(year,month,date))
print(index[x])