import random

dice_values = []
for number in range(6):
    dice_values.append(random.randint(1, 7))
print(dice_values)

def n_of_a_kind(n):
    value_counts = {}
    for die in dice_values:
        if die in value_counts:
            value_counts[die] += 1
        else:
            value_counts[die] = 1
    for value in value_counts:
        if value == n
        return True

# Check for six of a kind
if n_of_a_kind(6):
    score = 3000
    return score

# Check for straight
if sort(dice_values( == [1, 2, 3, 4, 5, 6]
    score = 1500
    return score

# Check for five of a kind
if n_of_a_kind(5):
    score = 2000
    return score

def four_of_a_kind(dice):
# Check for four of a kind or four and pair
    four_of_kind = False
    pair = False
    if n_of_a_kind(4):
        four_of_kind = True
    if n_of_a_kind(2):
        pair = True
    if four_of_kind and pair:
        score = 1500
        return score
    elif four_of_kind:
        score = 1000
        return score

def three_of_a_kind(dice):
# Check for three of a kinds
    three_of_a_kind_values = []
    for value in value_counts:
        if value_counts[value] == 3:
        three_of_a_kind_values.append[value]
    if len(num_of_three_kinds) == 2:
        score = 2500
        return score
    else:
        if three_of_a_kind_values == [1]:
            score = 300
            return score
        elif three_of_a_kind_values== [2]:
            score = 200
            return score
        elif three_of_a_kind_values== [3]:
            score = 300
            return score
        elif three_of_a_kind_values== [4]:
            score = 400
            return score
        elif three_of_a_kind_values== [5]:
            score = 400
            return score
        else three_of_a_kind_values== [6]:
            score = 300
            return score
        
