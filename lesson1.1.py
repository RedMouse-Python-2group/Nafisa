#!/usr/bin/env python
# -*- coding: utf-8 -*-
age = input("How old are you?\n")
if age <= 7:
    print("You are baby")
elif 7 < age <= 18:
    print("You should study in school")
elif 18 < age <= 25:
    print("Welcom to University")
elif 18 < age <= 60:
    print("Do you work?")
elif 60 < age <= 120:
    print("You can have a rest all day long")
else: 
    print("Warning! \n")*5
    print("This is programm for humans")
    
raw_input()