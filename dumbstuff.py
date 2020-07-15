# sort array in asc or desc
def sortlist(rawlist: list, operator: str, ifprint: bool):
    looped = 0
    done = 0
    index = 0
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
        if operator == ">":
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

    if ifprint:
        print(sortedList)

    return sortedList
