# def countdown(number):
#       numberList = []
#       for i in range(number,-1,-1):
#             if i <= 10:
#                   print(i)
#             numberList.append(i)
#       else:
#             return numberList


# x = countdown(10)
# print(x)

# def printReturn(list):
#       print(list[0])
#       return list[1]
# y = printReturn([1,5])
# print(y)

# def firstPlusLength(list):
#       sum = 0
#       for i in range(list[0],len(list),1):
#             if i <= len(list):
#                   x = len(list)
#                   print(x)
#                   sum += list[i]
#       return sum
# print(firstPlusLength([1,2,3,4,5]))

# def firstPlusLengthCorrected(list):
#       sum = list[0] + len(list)
#       return sum
# print(firstPlusLengthCorrected([10,15,30]))

# def valuesGreaterThanSecond(list):
#       newList = []
#       if len(list) < 2:
#             return False
#       else:
#             for i in range(0,len(list),1):
#                   if list[i] > list[1]:
#                         newList.append(list[i])
#       return newList
# print(valuesGreaterThanSecond([10,5,10,15,20]))
# print(valuesGreaterThanSecond([1]))

def thisLengthThatValue(size,value):
      list = []
      maxLength = size
      while len(list) < maxLength:
                  print(len(list))
                  list.append(value)
                  print(len(list))
      return list
print(thisLengthThatValue(10,1))