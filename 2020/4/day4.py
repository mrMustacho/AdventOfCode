# -*- coding: utf-8 -*-
"""
Created on 2020-12-23

@author: Alejandro
"""
# the class is kinda unnecessary but I wanted to play with classes anyways
class Passport:
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt 
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid       

def readFile(filename):
    with open(filename, "r") as file:
        rawdata = [str(line[:-1]) for line in file.readlines()]
        data = []
        for line in rawdata:
            if line != '':
                for field in line.split():
                    data.append(field)
            else:
                data.append(line)
        return data

# returns a list of passports, if the new from the fields is invalid, it returns the same passport list
def createPassport(fields, passports):
    try:
        byr, iyr, eyr, hgt, hcl, ecl, pid = None, None, None, None, None, None, None
        for field in fields:
            key = field[:3]
            value = field[4:]
            if key == 'byr' and value.isdigit() and 1920 <= int(value) and int(value) <= 2002:
                byr = value                            
            elif key == 'iyr' and value.isdigit() and 2010 <= int(value) and int(value) <= 2020:
                iyr = value                            
            elif key == 'eyr' and value.isdigit() and 2020 <= int(value) and int(value) <= 2030:
                eyr = value                           
            elif key == 'hgt':
                if value[-2] == 'c' and value[:-2].isdigit() and 150 <= int(value[:-2]) and int(value[:-2]) <= 193:
                    hgt = value
                if value[-2] == 'i' and value[:-2].isdigit() and 59 <= int(value[:-2]) and int(value[:-2]) <= 76:
                    hgt = value                         
            elif key == 'hcl' and value[0] == '#':
                index = 0
                isValid = 1
                for char in value[1:]:
                    if index > 6:
                        isValid = 0
                        break
                    if not (('a' <= char and char <= 'f') or (0 <= int(char) and int(char) <= 9)):
                        isValid = 0
                        break
                    index += 1
                if index != 6:
                    isValid = 0
                if isValid:
                    hcl = value                           
            elif key == 'ecl' and (value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth'):
                ecl = value                            
            elif key == 'pid':
                isValid = 1
                index = 0
                for char in value:
                    if index > 9:
                        isValid = 0
                        break
                    if not char.isdigit():
                        isValid = 0
                        break
                    index += 1
                if index != 9:
                    isValid = 0
                if isValid:
                    pid = value                            
        if byr == None or iyr == None or eyr == None or hgt == None or hcl == None or ecl == None or pid == None:
            return passports
        newPassport = Passport(byr, iyr, eyr, hgt, hcl, ecl, pid)
        passports.append(newPassport)
        return passports
    except:
        return passports

def isValid(fields):
    if len(fields) == 8:
        return 1
    elif len(fields) == 7:
        for field in fields:
            if field[:3] == 'cid':
                return 0
        return 1
    else:
        return 0

def part1(data):
    tempFields = []
    validPassports = 0
    for field in data:
        if field != '':
            tempFields.append(field)
        else:
            validPassports += isValid(tempFields)
            tempFields = []
    # This for loop doesn't check the las passport, so we need one last check
    validPassports += isValid(tempFields)  
    return validPassports

def part2(data):
    passports = []
    tempFields = []
    for field in data:
        if field != '':
            tempFields.append(field)
        else:
            passports = createPassport(tempFields, passports)
            tempFields = []
    # This for loop doesn't check the las passport, so we need one last check
    passports = createPassport(tempFields, passports)
    return len(passports)

def main():
    data = readFile("input.txt")
    print("Part 1: {} valid passports".format(part1(data)))
    print("Part 1: {} valid passports".format(part2(data)))

if __name__ == "__main__":
    main()
