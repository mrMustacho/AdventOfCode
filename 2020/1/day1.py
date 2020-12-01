# -*- coding: utf-8 -*-
"""
Created on 2020-12-01

@author: Alejandro
"""

def readFile() -> list:
    with open("input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

def part1(entries, leng):
    temp = []
    for i in range(leng):
        for j in range(i+1, leng):
            if entries[i] + entries[j] == 2020:
                temp.append(entries[i]*entries[j])
    return str(max(temp))

def part2(entries, leng):
    temp = []
    for i in range(leng):
        for j in range(i+1,leng):
            for k in range(j+1,leng):
                if entries[i] + entries[j] + entries[k] == 2020:
                    temp.append(entries[i] * entries[j] * entries[k])
    return str(max(temp))
    
def main():
    entries = readFile()
    leng = len(entries)
    print("part 1: " + part1(entries, leng))
    print("part 2: " + part2(entries, leng))

if __name__ == "__main__":
    main()
