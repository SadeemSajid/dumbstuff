import random

# sort list in asc or desc
def sortlist(rawlist: list, operator: str, ifprint: bool):
    looped = 0
    done = 0
    index = 0
    unsortedlist = rawlist
    sortedList = []

    while done == 0:
        index = 0
        looped = 0

        # ascending sort
        if operator == "<":
            while index < len(rawlist) - 1:
                if rawlist[index] > rawlist[index + 1]:
                    temp = rawlist[index]
                    rawlist[index] = rawlist[index + 1]
                    rawlist[index + 1] = temp
                    looped += 1
                index += 1
            if looped == 0:
                done = 1
            sortedList = rawlist
        # descending sort
        elif operator == ">":
            while index < len(rawlist) - 1:
                if rawlist[index] < rawlist[index + 1]:
                    temp = rawlist[index + 1]
                    rawlist[index + 1] = rawlist[index]
                    rawlist[index] = temp
                    looped += 1
                index += 1
            if looped == 0:
                done += 1
            sortedList = rawlist
        else:
            done = 1
            sortedList = unsortedlist
    if ifprint:
        print(sortedList)

    return sortedList


# jumble list elements randomly
def jumblelist(rawlist: list):
    index = 0
    counter = 0
    jumbledlist = []

    jumble = True
    while counter < len(rawlist):
        i1 = random.randint(0, len(rawlist) - 1)
        i2 = random.randint(0, len(rawlist) - 1)
        temp = rawlist[i1]
        rawlist[i1] = rawlist[i2]
        rawlist[i2] = temp
        counter += 1

    jumbledlist = rawlist
    return jumbledlist


