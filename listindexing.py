import copy

my_list = [1,2,3,4,5,6,7,8,9,10]

def loop_list(lst):
    for element in lst:
        print(element)

print(my_list[:-1]) # wszystko do ostatniego elementu
print(my_list[-1:]) # ostatni element
print(my_list[::2]) # co drugi element

#######################

# List comprhensions - Wyrażenia listowe
print("\n")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print('classic for-loop:',newlist)

newlist_list_comprehension = [x for x in fruits if "a" in x]
print('list comprehension:', newlist_list_comprehension)



numbers_to_divide = range(1,1000)
example1 = [x * 0.1 for x in numbers_to_divide]

newlist = []
for x in numbers_to_divide:
    newlist.append(x * 0.1)

##########
print('\n')
x = [1,2]
y = x
print("X i Y takie same obiekty w pamieci",id(x) == id(y))
x = [2,53]
print("X i Y rozne obiekty w pamieci",id(x) == id(y))
x1 = copy.deepcopy(y)
x = y # znowu takie same obiekty w pamici
x.pop() # edycja  obiektu w pamieci zmienia i X i Y
print(x,y,x1)
