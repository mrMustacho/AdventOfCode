# -*- coding: utf-8 -*-
"""
Created on 2020-12-02

@author: Alejandro
"""

import re

def readFile(filename):
    data = []
    p = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    with open(filename, "r") as file:
        for line in file.readlines():
            temp = p.split(line)
            input = []
            for i in range(1,5):
                group = temp[i]
                if group.isdigit():
                    input.append(int(group))
                else:
                    input.append(group)
            data.append(input)
    return data

def part1(data): # return the number of valid pwds
    validPwds = 0
    for field in data:
        ocurrence = 0
        for char in field[3]: # pwd 
            if char == field[2]: # must have letter
                ocurrence += 1
        if field[0] <= ocurrence and ocurrence <= field[1]:
            validPwds += 1
    return validPwds

def part2(data): # return the number of valid pwds
    validPwds = 0
    for field in data:
        if (field[3][field[0]-1] == field[2]) ^ (field[3][field[1]-1] == field[2]):
            validPwds += 1
    return validPwds

def main():
    data = readFile("input.txt")
    print("Part 1: There are {} valid passwords".format(part1(data)))
    print("Part 2: There are {} valid passwords".format(part2(data)))

if __name__ == "__main__":
    main()
