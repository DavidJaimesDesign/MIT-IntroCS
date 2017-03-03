#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:57:00 2017

@author: davidjaimes
"""
annual_salary = input("Your yearly salary: ")
portion_saved = input("How much do you want to save(ex 10% 0.1): ")
total_cost = input("Cost of your dream home: ")

portion_down_payment = total_cost/4

current_savings = 0
r = 0.04

monthly_savings = annual_salary*portion_saved/12
monthly_roi = current_savings*r/12
months = 0

while(current_savings < portion_down_payment):
    months += 1
    current_savings += monthly_savings + current_savings*r/12
    
print ("It would take you: " + str(months))
    