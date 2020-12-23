# -*- coding: utf-8 -*-
"""
Created on 2020-12-22

@author: Alejandro
"""

def readFile(filename):
    with open(filename, "r") as file:
        return [str(line[:-1]) for line in file.readlines()]

def slope(map, right, down):
    treesEncountered = 0
    xposition = 0
    for index in range(0,len(map),down):
        xposition += right
        if index + down < len(map) and map[index + down][xposition%len(map[0])] == '#':
            treesEncountered += 1
    return treesEncountered

def part1(map):
    return slope(map,3,1)

def part2(map):
    return slope(map,1,1) * slope(map,3,1) * slope(map,5,1) * slope(map,7,1) * slope(map,1,2)

def main():
    map = readFile("input.txt")
    print("Part 1: {} trees encountered".format(part1(map)))
    print("Part 2: {} trees encountered".format(part2(map)))

if __name__ == "__main__":
    main()