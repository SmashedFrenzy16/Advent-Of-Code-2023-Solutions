
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

            

    print(score)