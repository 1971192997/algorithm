from randomList import randomList

iList = randomList(20)


def bubble_sort(iList):
    if len(iList) <= 1:
        return iList
    for i in range(1, len(iList)):
        for j in range(0, len(iList) - i):
            if iList[j] > iList[j + 1]:
                iList[j], iList[j + 1] = iList[j + 1], iList[j]
    return iList


if __name__ == '__main__':
    print(iList)
    print(bubble_sort(iList))
