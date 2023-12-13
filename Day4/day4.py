
with open("puzzle_input.txt") as f:

    file = f.read().splitlines()

    score = 0

    def num_arr(line, num, letter):

        return [int(letter) for letter in line.split(":")[1].split("|")[int(num)].split()]


    for line in file:

        user_nums = num_arr(line, 1, "u")
        winning_nums = num_arr(line, 0, "w")

        indiv_point = 0

        power = 0

        for u in user_nums:

            if u in winning_nums:

                indiv_point = 2 ** power

                power += 1

        score += indiv_point

    score2 = 0

    def iterated(matching_nums, file):

        return range(i + 1, min(i + len(matching_nums) + 1, len(file)))

    add_1 = 1

    mult = [add_1 for i in file]

    for i, line in enumerate(file):

        user_nums = num_arr(line, 1, "u")
        winning_nums = num_arr(line, 0, "w")

        matching_nums = [m for m in user_nums if m in winning_nums]

        for copy in iterated(matching_nums, file):

            mult[copy] += mult[i]

        score2 += mult[i]

            

    print(f"Part 1 Solution: {score}")

    print(f"Part 2 Solution {score2}")
