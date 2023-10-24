ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4',['list', 'in', 'a' 'list'], 987]
empty_list = []
print(my_list[2])

# adding lists togeher
fruits = ['apple', 'banana', 'orange', "strawberry"]
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)


salad = 3 * vegetables
print(salad)
#            0            1           2
drawers = ['documents', 'envelopes', 'pens']

## were replacing
drawers[0] = 'digital documents'
best_content  = drawers[0]
print()
drawers[1] = drawers[2]
print(drawers[1])

nums = [1,2,3,4,5,]
nums.append(45)
print(nums)
## this colon thing inclusively selects a range that you want the list to print or modify
words = ['start', 'going', 'till','the','end']
print(words[0:3])
print(words[:3])
print(words[2:4])

copy_of_words = words[:]
print(copy_of_words)
copy_of_words.append('dojo')
print(copy_of_words)

your_list = ['cookies', 'ice cream', 'soda' 'brownies']
print(len(your_list))

number_list = [1,2,3,4,5,100, -1]
print(max(number_list))

list2 = ['zebra','elephant','giraffe', 'alpacka']
print(sorted(list2))

list2.pop()
print(list2)
list2.append('cat')
print(list2)
print(list2.index('cat'))
list2.reverse()
print(list2)