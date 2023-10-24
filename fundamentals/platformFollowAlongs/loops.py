# for i in range(5):
#       print(i)

# for e in range(1,10):
#       print(e)

# for n in range(0,50,5):
#       print('step', n)

# # negative - decreases

# for k in range(1000,500,-100):
#       print('loop pass', k)

# looping through arrays
wordTest = "hello"
for c in wordTest:
      print(c)

my_list = ['abc', 54, 'xm']
for objects in range(0, len(my_list)):
      print(objects, my_list[objects])

your_list = ['mommy','daddy', 'brother']
for names in your_list:
      count = 0
      count = count + 1
      print(names, count)

count = 0
while count <= 5:
      print('looping - ', count)
      count += 1

count2 = 100
while count2 > 50:
      print('loop -', -count2)
      count2 -= 1

count3 = 400
while count3 > 0:
      print(count3)
      count3 = count3 - 99
else:
      print('this will be the last print statement')

# useage of a break:

for i in "dadisinthehouse":
      if i == 'i':
            break
      print(i)

for i in "momisinthehouse":
      if i == 'i':
            continue
      print(i)

y = 5
while y > 0:
      print(y)
      y = y -1
      if y == 0:
            break
else:
      print('this should not print')