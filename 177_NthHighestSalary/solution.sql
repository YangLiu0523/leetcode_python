#!/usr/bin/env python
# coding=utf-8
#
# Title: 177. Nth Highest Salary
# Author: Lucas
# Date: 2018-05-30 21:54:18
#
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      SELECT DISTINCT Salary FROM Employee GROUP BY Salary
      ORDER BY Salary DESC LIMIT 1 OFFSET N
  );
END
