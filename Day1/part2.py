import re

with open("puzzle_input.txt") as f:
    
    file = f.read().strip()

    file = file.split("\n")

    letter_to_num = {"oneight": "18", "twone": "21", "threeight": "38", "fiveight": "58", "eightwo": "82", "eighthree": "83", "nineight": "98", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

    replaced_content = ""

    for line in file:
        
        line = line.strip()

        for og, new in letter_to_num.items():
            line = re.sub(og, new, line)

        replaced_content = f"{replaced_content}{line}\n"

    write_file = open("puzzle_input.txt", "w")

    write_file.write(replaced_content)


    def a_num(i):

        if i.isdigit():

            return i
    
    def reverse(s):

        return s[::-1]

    num_sum = 0
    f_digit = 0
    l_digit = 0

    for line in file:

        print(line)

        for char in range(len(line)):

            if a_num(line[char]):

                f_digit = line[char]

                break

        for char in range(len(reverse(line))-1, -1, -1):

            if a_num(line[char]):

                l_digit = line[char]

                break
        
        num_sum += int(f_digit + l_digit)

        f_digit = 0
        l_digit = 0

    print(num_sum)
