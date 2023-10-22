# Basic - Print all integers from 0 to 150. - COMPLETED - Lines - 8-9
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000 - COMPLETE - Lines - 11-12
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo". -- COMPLETED - Lines 14 - 20
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum. - COMPLETED - Lines 22 - 27
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours. -- COMPLETED - Lines 29 - 30
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines) - Completed - Lines 32 - 37

for i in range(0, 151):
    print(i)

for n in range(5, 1005, 5):
    print(n)

for e in range(1, 101):
    if e % 10 == 0:
        print("Coding Dojo")
    elif e % 5 == 0:
        print("Coding")
    else:
        print(e)

sums = 0
for odds in range(0, 500000):
    if odds % 2 == 1:
        sums += odds

print(sums)

for i in range(2018, 0, -4):
      print(i)

def flexCounter(lowNumb,highNumb,mult):
      for i in range(lowNumb,highNumb):
            if i % mult == 0:
                  print(i)

flexCounter(3,50,2)