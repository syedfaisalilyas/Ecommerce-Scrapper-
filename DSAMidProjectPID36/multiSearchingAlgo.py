from datetime import datetime


def linearSearch(arr, target, filter):
    if filter == "Contains":
        return linearSearchContains(arr, target)
    elif filter == "Equals" or filter == "On":
        return linearSearchEquals(arr, target)
    elif filter == "Starts With":
        return linearSearchStartsWith(arr, target)
    elif filter == "Ends With":
        return linearSearchEndsWith(arr, target)
    elif filter == "Greater Than":
        return linearSearchGreaterThan(arr, target)
    elif filter == "Less Than":
        return linearSearchLessThan(arr, target)
    elif filter == "Before":
        return linearSearchBefore(arr, target)
    elif filter == "After":
        return linearSearchAfter(arr, target)


def linearSearchEquals(arr, target):
    res = []
    for i in range(0, len(arr)):
        if type(target)(arr[i]) == type(target)(target):
            res.append(i)
    return res


def linearSearchGreaterThan(arr, target):
    res = []
    for i in range(0, len(arr)):
        if int(arr[i]) > int(target):
            res.append(i)
    return res


def linearSearchLessThan(arr, target):
    res = []
    for i in range(0, len(arr)):
        if int(arr[i]) < int(target):
            res.append(i)
    return res


def dateConversion(date):
    date = date.split("/")
    return datetime(int(date[2]), int(date[0]), int(date[1]))


def linearSearchBefore(arr, target):
    res = []
    target = dateConversion(target)
    for i in range(0, len(arr)):
        arr[i] = dateConversion(arr[i])
        if (arr[i]) < (target):
            res.append(i)
    return res


def linearSearchAfter(arr, target):
    res = []
    target = dateConversion(target)
    for i in range(0, len(arr)):
        arr[i] = dateConversion(arr[i])
        if (arr[i]) > (target):
            res.append(i)
    return res


def linearSearchContains(arr, target):
    res = []
    for i in range(0, len(arr)):
        if target in arr[i]:
            res.append(i)
    return res


def linearSearchEndsWith(arr, target):
    res = []
    for i in range(0, len(arr)):
        if arr[i].endswith(target):
            res.append(i)
    return res


def linearSearchStartsWith(arr, target):
    res = []
    for i in range(0, len(arr)):
        if arr[i].startswith(target):
            res.append(i)
    return res


def binarySearch(arr, target, filter):
    return [binarySearchMain(arr, 0, len(arr), target)]


def binarySearchMain(arr, left, right, target):
    if right >= left:
        mid = left+(right-left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearchMain(arr, left, mid-1, target)
        else:
            return binarySearchMain(arr, mid+1, right, target)
    else:
        return -1


def jumpSearch(arr, target, filter):
    # if filter == "Contains":
    #     return jumpSearchContains(arr, target)
    # if filter == "Equals" or filter == "On":
    #     return jumpSearchEquals(arr, target)
    # elif filter == "Starts With":
    #     return linearSearchStartsWith(arr, target)
    # elif filter == "Ends With":
    #     return linearSearchEndsWith(arr, target)
    if filter == "Greater Than":
        return jumpSearchGreaterThan(arr, target)
    elif filter == "Less Than":
        return jumpSearchLessThan(arr, target)
    # elif filter == "Before":
    #     print(filter)
    #     return jumpSearchBefore(arr, target)
    # elif filter == "After":
    #     return jumpSearchAfter(arr, target)


# def jumpSearchContains(arr, target):
#     arr.sort()
#     #print(arr, len(arr))
#     res = []
#     step = int(len(arr)**0.5)
#     for i in range(0, len(arr), step):
#         if target in arr[i]:
#             res.append(i)
#         elif arr[i] < target:
#             # print(arr[i])
#             for j in range(i-step, i):
#                 if target in arr[j]:
#                     res.append(j)
#     return res


# print(jumpSearchContains(
#     ["NotdVEVO",
#      "Karina Arakelyan",
#      "Camila Coelho",
#      "TV Promos",
#      "Tim & Chia Vlogs",
#      "TheGamer",
#      "BabyFirst Learn Colors, ABCs, Rhymes & More",
#      "Sorrow TV",
#      "PowerDrift",
#      "Teni Panosian",
#      "kawaiisweetworld",
#      "Baby Kaely",
#      "Hacktuber",
#      "Yiannimize",
#      "Whistle",
#      "SAARA",
#      "BFA",
#      "Beautycanbraid",
#      "AlfredoOlivasVEVO",
#      "A Plus Entertainment",
#      "Alamidral",
#      "BarsAndMelodyVEVO"
#      "Melissa Samways",
#      "vicentefernandezVEVO"
#      ], "VEVO"))

def jumpSearchMain(arr, target, type):
    step = int(len(arr)**0.5)
    for i in range(0, len(arr), step):
        if type(arr[i]) == type(target):
            return i
        elif type(arr[i]) > type(target):
            for j in range(i-step, i):
                if type(arr[j]) == type(target):
                    return j


#print(jumpSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 23, 24], 10))


# def jumpSearchEquals(arr, target):
#     idxStart = jumpSearchMain(arr, target)
#     c = arr.count(target)
#     print(idxStart, c)
#     indices = [x for x in range(idxStart-c, idxStart+c)]
#     return indices


def jumpSearchGreaterThan(arr, target):
    idx = jumpSearchMain(arr, target, int)
    indices = [x for x in range(idx+1, len(arr))]
    return indices


def jumpSearchLessThan(arr, target):
    idx = jumpSearchMain(arr, target, int)
    indices = [x for x in range(0, idx)]
    return indices


# def jumpSearchBefore(arr, target):
#     target = dateConversion(target)
#     idx = jumpSearchMain(arr, target, dateConversion)
#     print(idx)
#     indices = [x for x in range(0, idx)]
#     return indices


# def jumpSearchAfter(arr, target):
#     target = dateConversion(target)
#     idx = jumpSearchMain(arr, target, dateConversion)
#     print(idx)
#     indices = [x for x in range(idx+1, len(arr))]
#     return indices


def exponentialSearch(arr, target, filter):
    if arr[0] == target:
        return [0]
    i = 1
    while arr[i] <= target and i < len(arr):
        i *= 2
    return [binarySearch(arr, i//2, min(i, len(arr)-1), target)]
