import random

stone_list = list(range(53)) * 2  # Creating Stones
stone_list_p1 = list()  # Creating Hand of Player 1
stone_list_p2 = list()  # Creating Hand of Player 2
stone_list_p3 = list()  # Creating Hand of Player 3
stone_list_p4 = list()  # Creating Hand of Player 4
remaining_p1 = list()   # Remaining Hand of Player 1
remaining_p2 = list()   # Remaining Hand of Player 2
remaining_p3 = list()   # Remaining Hand of Player 3
remaining_p4 = list()   # Remaining Hand of Player 4
splitting_stones = list(range(4))  # A list for determining which player starts with 15 stones
indicator_stone = 52
okey_stone = 0

random.shuffle(stone_list)  # Shuffling the stones
print("Shuffling the stones.\n")

# Checking if indicator stone is fake okey and pulling a new one if its fake okey
while indicator_stone == 52:
    # Selecting the indicator stone and removing it from the deck
    indicator_stone = random.choice(stone_list)
stone_list.pop(stone_list.index(indicator_stone))

# Selecting the okey stone
if indicator_stone == 12 or indicator_stone == 25 or indicator_stone == 38 or indicator_stone == 51:
    okey_stone = indicator_stone - 12

else:
    okey_stone = indicator_stone + 1

# Determining which player going to get 15 stones
random_stone = random.choice(splitting_stones)
splitting_stones.pop(splitting_stones.index(random_stone))
stones_p1 = random_stone
random_stone = random.choice(splitting_stones)
splitting_stones.pop(splitting_stones.index(random_stone))
stones_p2 = random_stone
random_stone = random.choice(splitting_stones)
splitting_stones.pop(splitting_stones.index(random_stone))
stones_p3 = random_stone
random_stone = random.choice(splitting_stones)
splitting_stones.pop(splitting_stones.index(random_stone))
stones_p4 = random_stone

if stones_p1 < 3:
    stones_p1 = 0
else:
    stones_p1 = 1

if stones_p2 < 3:
    stones_p2 = 0
else:
    stones_p2 = 1

if stones_p3 < 3:
    stones_p3 = 0
else:
    stones_p3 = 1

if stones_p4 < 3:
    stones_p4 = 0
else:
    stones_p4 = 1

# Splitting the stones
while len(stone_list_p1) < 14 + stones_p1:
    random_stone = random.choice(stone_list)
    stone_list_p1.append(stone_list.pop(stone_list.index(random_stone)))
while len(stone_list_p2) < 14 + stones_p2:
    random_stone = random.choice(stone_list)
    stone_list_p2.append(stone_list.pop(stone_list.index(random_stone)))
while len(stone_list_p3) < 14 + stones_p3:
    random_stone = random.choice(stone_list)
    stone_list_p3.append(stone_list.pop(stone_list.index(random_stone)))
while len(stone_list_p4) < 14 + stones_p4:
    random_stone = random.choice(stone_list)
    stone_list_p4.append(stone_list.pop(stone_list.index(random_stone)))

# Replacing okey stone with 53 for giving it special properties later
for i in range(2):
    if okey_stone in stone_list_p1:
        stone_list_p1.pop(stone_list_p1.index(okey_stone))
        stone_list_p1.append(53)
    if okey_stone in stone_list_p2:
        stone_list_p2.pop(stone_list_p2.index(okey_stone))
        stone_list_p2.append(53)
    if okey_stone in stone_list_p3:
        stone_list_p3.pop(stone_list_p3.index(okey_stone))
        stone_list_p3.append(53)
    if okey_stone in stone_list_p4:
        stone_list_p4.pop(stone_list_p4.index(okey_stone))
        stone_list_p4.append(53)

# Replacing fake okeys with okey stone values
for i in range(2):

    if 52 in stone_list_p1:
        stone_list_p1.pop(stone_list_p1.index(52))
        stone_list_p1.append(okey_stone)

    if 52 in stone_list_p2:
        stone_list_p2.pop(stone_list_p2.index(52))
        stone_list_p2.append(okey_stone)

    if 52 in stone_list_p3:
        stone_list_p3.pop(stone_list_p3.index(52))
        stone_list_p3.append(okey_stone)

    if 52 in stone_list_p4:
        stone_list_p4.pop(stone_list_p4.index(52))
        stone_list_p4.append(okey_stone)

# Counting the okey stones(which is always 53) of players
okey_count_p1 = stone_list_p1.count(53)
okey_count_p2 = stone_list_p2.count(53)
okey_count_p3 = stone_list_p3.count(53)
okey_count_p4 = stone_list_p4.count(53)

# Removing okey stones from players hands
for i in range(2):
    if 53 in stone_list_p1:
        stone_list_p1.pop(stone_list_p1.index(53))
    if 53 in stone_list_p2:
        stone_list_p2.pop(stone_list_p2.index(53))
    if 53 in stone_list_p3:
        stone_list_p3.pop(stone_list_p3.index(53))
    if 53 in stone_list_p4:
        stone_list_p4.pop(stone_list_p4.index(53))

# Doubles Win Condition
# Find and remove dupes from a list for the Doubles win condition
dup_set = {x for x in stone_list_p1 if stone_list_p1.count(x) > 1}
dup_list = list(dup_set) * 2
no_dupes_list_p1 = [x for x in stone_list_p1 if x not in dup_list]

dup_set = {x for x in stone_list_p2 if stone_list_p2.count(x) > 1}
dup_list = list(dup_set) * 2
no_dupes_list_p2 = [x for x in stone_list_p2 if x not in dup_list]

dup_set = {x for x in stone_list_p3 if stone_list_p3.count(x) > 1}
dup_list = list(dup_set) * 2
no_dupes_list_p3 = [x for x in stone_list_p3 if x not in dup_list]

dup_set = {x for x in stone_list_p4 if stone_list_p4.count(x) > 1}
dup_list = list(dup_set) * 2
no_dupes_list_p4 = [x for x in stone_list_p4 if x not in dup_list]

# Points of players for Doubles win condition
doubles_point_p1 = len(no_dupes_list_p1) - okey_count_p1
doubles_point_p2 = len(no_dupes_list_p2) - okey_count_p2
doubles_point_p3 = len(no_dupes_list_p3) - okey_count_p3
doubles_point_p4 = len(no_dupes_list_p4) - okey_count_p4


# Series Win Condition
# Remove the consecutive numbers from the list
def is_valid(n, seq, group):
    is_in_group = True if len(group) != 0 and group[0] <= n <= group[-1] else False
    if not is_in_group:
        return False
    return len(seq) == 0 or seq[-1] + 1 == n or n == seq[0]


def get_group(i, groups):
    for g in groups:
        if g[0] <= i <= g[-1]:
            return g
    return []


def clean(lst, groups):
    lst.sort()
    seq = []
    previous_group = groups[0]
    to_remove = []
    for v in lst:
        c_group = get_group(v, groups)
        if previous_group != c_group:
            # remove the seq from the input list here
            if len(seq) > 3:
                to_remove += seq
            seq = []
        if is_valid(v, seq, c_group):
            seq += [v]
        previous_group = c_group

    if len(seq) > 3:
        to_remove += seq

    for i in to_remove:
        lst.remove(i)
    return lst


groups = [
    [i for i in range(13)],
    [i for i in range(13, 25)],
    [i for i in range(25, 38)],
    [i for i in range(38, 51)]
]

result_list_1_p1 = clean(stone_list_p1, groups)
result_list_1_p2 = clean(stone_list_p2, groups)
result_list_1_p3 = clean(stone_list_p3, groups)
result_list_1_p4 = clean(stone_list_p4, groups)


# Removing same numbered stones with different colors
def series_split(lst: list):
    values = [{} for _ in range(13)]

    for n in lst:
        rem = n % 13
        if n not in values[rem]:
            values[rem][n] = 1
        else:
            values[rem][n] += 1

    for same_rem_vals in values:
        if len(same_rem_vals) < 3:
            continue

        min_repeating = min(same_rem_vals.values())
        for n in same_rem_vals:
            same_rem_vals[n] -= min_repeating

    new_lst = []
    for same_rem_vals in values:
        for value, times in same_rem_vals.items():
            for _ in range(times):
                new_lst.append(value)

    return new_lst


result_list_2_p1 = series_split(result_list_1_p1)
result_list_2_p2 = series_split(result_list_1_p2)
result_list_2_p3 = series_split(result_list_1_p3)
result_list_2_p4 = series_split(result_list_1_p4)

# Points of players for Series win condition
series_point_p1 = len(result_list_2_p1)
series_point_p2 = len(result_list_2_p2)
series_point_p3 = len(result_list_2_p3)
series_point_p4 = len(result_list_2_p4)

# Calculating the player closest to the win
if doubles_point_p1 < series_point_p1:
    point_p1 = doubles_point_p1
    remaining_p1 = no_dupes_list_p1
else:
    point_p1 = series_point_p1
    remaining_p1 = result_list_2_p1

if doubles_point_p2 < series_point_p2:
    point_p2 = doubles_point_p2
    remaining_p2 = no_dupes_list_p2
else:
    point_p2 = series_point_p2
    remaining_p2 = result_list_2_p2

if doubles_point_p3 < series_point_p3:
    point_p3 = doubles_point_p3
    remaining_p3 = no_dupes_list_p3
else:
    point_p3 = series_point_p3
    remaining_p3 = result_list_2_p3

if doubles_point_p4 < series_point_p4:
    point_p4 = doubles_point_p4
    remaining_p4 = no_dupes_list_p4
else:
    point_p4 = series_point_p4
    remaining_p4 = result_list_2_p4

finding_min = (point_p1, point_p2, point_p3, point_p4)
winner = finding_min.index(min(finding_min))



# Sorting players hands
remaining_p1.sort()
remaining_p2.sort()
remaining_p3.sort()
remaining_p4.sort()

# Printing the results after splitting stones
print(f'Indicator Stone: {indicator_stone}')
print(f'Okey Stone: {okey_stone}\n')
print(f'Remaining Stones of Player 1:{remaining_p1} How many stones left: {point_p1}')
print(f'Remaining Stones of Player 2:{remaining_p2} How many stones left: {point_p2}')
print(f'Remaining Stones of Player 3:{remaining_p3} How many stones left: {point_p3}')
print(f'Remaining Stones of Player 4:{remaining_p4} How many stones left: {point_p4}\n')
print(f'Player closest to the winning is: Player {winner + 1}')
