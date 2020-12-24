# -*- coding: utf-8 -*-
"""
Created on 2020-12-24

@author: Alejandro
"""

def readFile(filename):
    with open(filename, "r") as file:
        return [str(line[:-1]) for line in file.readlines()]

def getRow(seat):
    bottom = 0
    top = 127
    mid = int(top/2)
    for char in seat[:][:7]:
        if char == "F":
            # lower half
            top = mid
            mid = int((top+bottom)/2)
        else:
            # upper half
            bottom = mid + 1
            mid = int((top+bottom)/2)
    return top

def getCol(seat):
    bottom = 0
    top = 7
    mid = int(top/2)
    for char in seat[:][7:]:
        if char == "L":
            # lower half
            top = mid
            mid = int((top+bottom)/2)
        else:
            # upper half
            bottom = mid + 1
            mid = int((top+bottom)/2)
    return top

def getID(row, col):
    return row * 8 + col

def getPositions(data):
    seats = []
    for seat in data:
        row = getRow(seat)
        col = getCol(seat)
        ID = getID(row, col)
        seats.append([row, col, ID])
    return seats

def part1(seats):
    maxID = 0
    for seat in seats:
        ID = seat[2]
        if maxID < ID:
            maxID = ID
    return maxID

def part2(seats):
    myID = None
    IDs = [i[2] for i in seats]
    IDs.sort()
    for i in range(len(IDs) - 1):
        diff = IDs[i+1] - IDs[i]
        if diff == 2:
            return IDs[i] + 1
    return None

def main():
    data = readFile("input.txt")
    seats = getPositions(data)
    print("Part 1: highest ID is {}".format(part1(seats)))
    print("Part 2: my ID is {}".format(part2(seats)))

if __name__ == "__main__":
    main()