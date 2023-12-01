with open("puzzle_input.txt") as f:
    
    file = f.read().strip()

    file = file.split("\n")

    def a_num(i):

        if i.isdigit():

            return i
    
    def reverse(s):

        return s[::-1]

    num_sum = 0
    f_digit = 0
    l_digit = 0

    for line in file:

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



