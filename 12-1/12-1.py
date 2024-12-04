from collections import Counter

# Part One
def total_distance(list1, list2):
    list1.sort()
    list2.sort()

    total_distance = 0

    for leftNum, rightNum in zip(list1, list2):
        total_distance += abs(leftNum - rightNum)

    return total_distance

list1 = []
list2 = []

# Part Two
def similarity_score(list1, list2):
    list2 = Counter(list2)
    similarity_score = 0

    for num in list1:
        similarity_score += num * list2[num]
    return similarity_score

inputFile = open("./input.txt", "r")
for line in inputFile:
    leftNum, rightNum = line.split()
    list1.append(int(leftNum))
    list2.append(int(rightNum))
print(total_distance(list1, list2))
print(similarity_score(list1, list2))
