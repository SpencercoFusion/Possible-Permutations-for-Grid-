import math as m

horizontal_width = 17
vertical_hight = 9
total_backsteps = 3

list_of_possible_permutations = []

def getPossiblePermutations(lefts, downs):
    ups = vertical_hight + downs - 1
    rights = horizontal_width + lefts - 1
    possible_permutations = ((m.factorial(ups + rights + lefts + downs)) 
                            /(m.factorial(ups) * m.factorial(downs) * m.factorial(rights) * m.factorial(lefts)))
    return possible_permutations
#~~~~~~~~~~~~~~~~~~~~~~~~~~~#
lefts = 0
downs = 0
total_permutations = 0

for i in range(total_backsteps + 1):
    lefts = i
    downs = 0
    for t in range(total_backsteps + 1):
        if (lefts + t) <= total_backsteps:
            downs = t
            this_permutations_count = [("lefts=" + str(lefts)), ("downs=" + str(downs)), getPossiblePermutations(lefts, downs)]
            list_of_possible_permutations.append(this_permutations_count)
        else:
            #print("failed at  LEFTS = " + str(lefts) + "  DOWNS = " + str(downs + 1))
            pass

for i in range(len(list_of_possible_permutations)):
    total_permutations += list_of_possible_permutations[i][2]

print(list_of_possible_permutations)
print("NUMBER OF SETS: " + str(len(list_of_possible_permutations)))
print("TOTAL PERMUTATIONS: " + str(total_permutations))