import random

dice_values = []
for number in range(6):
    dice_values.append(random.randint(1, 7))

def create_value_count_dict(dice_values):
    value_counts = {}
    for die in dice_values:
        if die in value_counts:
            value_counts[die] += 1
        else:
            value_counts[die] = 1
    return value_counts

def n_of_a_kind(n, value_counts):
    for value in value_counts:
        if value_counts[value] == n:
            return True

def score_of_1s(value_counts):
    if 1 in value_counts and (value_counts[1] == 1 or value_counts[1] == 2):
        if value_counts[1] == 1:
            score = 100
        else:
            score = 200
    else:
        score = 0
    return score

def score_of_5s(value_counts):
    if 5 in value_counts and (value_counts[5] == 1 or value_counts[5] == 2):
        if value_counts[5] == 1:
            score = 50
        else:
            score = 100
    else:
        score = 0
    return score

def three_of_a_kind(value_counts):
# Check for three of a kinds
    three_of_a_kind_values = []
    for value in value_counts:
        if value_counts[value] == 3:
            three_of_a_kind_values.append(value)
    if len(three_of_a_kind_values) == 2:
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
        elif three_of_a_kind_values== [6]:
            score = 300
            return score

def four_of_a_kind(value_counts):
# Check for four of a kind or four and pair
    four_of_kind = False
    pair = False
    if n_of_a_kind(4, value_counts):
        four_of_kind = True
    if n_of_a_kind(2, value_counts):
        pair = True
    if four_of_kind and pair:
        score = 1500
        return score
    elif four_of_kind:
        score = 1000
        return score

def calculate_score(dice_values):
    value_counts = create_value_count_dict(dice_values)
    # Check for six of a kind
    if n_of_a_kind(6, value_counts):
        score = 3000
        return score
    # Check for straight
    elif sorted(dice_values) == [1, 2, 3, 4, 5, 6]:
        score = 1500
        return score
    # Check for five of a kind
    elif n_of_a_kind(5, value_counts):
        score = 2000
        score += score_of_1s() + score_of_5s()
        return score
    elif four_of_a_kind(value_counts):
        score = four_of_a_kind(value_counts)
        if score == 1000:
            score += score_of_1s() + score_of_5s()
        return score
    elif three_of_a_kind(value_counts):
        score = three_of_a_kind(value_counts)
        if score != 2500:
            score += score_of_1s(value_counts) + score_of_5s(value_counts)
        return score
    else:
        score = score_of_1s(value_counts) + score_of_5s(value_counts)
        return score

print dice_values
print calculate_score(dice_values)
        
