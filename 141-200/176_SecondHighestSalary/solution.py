#!/usr/bin/env python
# coding=utf-8
#
# Title: 176. Second Highest Salary
# Author: Lucas
# Date: 2018-05-30 21:26:31
#
# Write your MySQL query statement below
SELECT max(Salary)
AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN
(SELECT max(Salary) from Employee);
