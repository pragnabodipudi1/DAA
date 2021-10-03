
def binarySearch(inputList, target):
    first = 0
    last = len(inputList)-1

    while(first <= last):
        midPoint = (first + last) // 2
        if inputList[midPoint] == target:
            return midPoint
        elif inputList[midPoint] < target:
            first = midPoint + 1
        else:
            last = midPoint - 1
    return None

inputList = [1,2,3,4,5,6,7,8,9,10]
target = 2

print(binarySearch(inputList, target))

