
with open("puzzle_input.txt") as f:

    file = f.read().splitlines()

    score = 0


    for line in file:

        user_nums = [int(u) for u in line.split(":")[1].split("|")[1].split()]
        winning_nums = [int(w) for w in line.split(":")[1].split("|")[0].split()]

        indiv_point = 0

        power = 0

        for u in user_nums:

            if u in winning_nums:

                indiv_point = 2 ** power

                power += 1

        score += indiv_point

    score2 = 0

    mult = [1 for i in file]

    for i, line in enumerate(file):

        user_nums = [int(u) for u in line.split(":")[1].split("|")[1].split()]
        winning_nums = [int(w) for w in line.split(":")[1].split("|")[0].split()]

        matching_nums = [m for m in user_nums if m in winning_nums]

        
        c_mult = mult[i]

        for j in range(i + 1, min(i + len(matching_nums) + 1, len(file))):

            mult[j] += c_mult

        score2 += c_mult

            

    print(f"Part 1 Solution: {score}")

    print(f"Part 2 Solution {score2}")
