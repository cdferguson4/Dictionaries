phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(type(phonebook))

print(phonebook['Chris'])

print(phonebook['John'])

print()
print('*****  end section 1 ********')
print()







print()
print('*****  start section 2 - search dictionary ********')
print()


if 'Chri' in phonebook:
    print(phonebook['Chris'])
else:
    print("Name does not exist")



print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Chris'] = '555-0123'

phonebook['Joe'] = '555-9999'

print(phonebook)





print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook['Chris']

print(phonebook)
print(len(phonebook))




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

for key in phonebook:
    print(key)
    print(phonebook[key])



print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

for value in phonebook.values():
    print(value)


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for k,v in phonebook.items():
    print("The key is: " + k + " The value is " + v)

for item_tuple in phonebook.items():
    print(item_tuple)
    print(type(item_tuple))


print(phonebook.get('Chris','Name does not exist'))



print()
print('*****  end section 7 ********')
print()

'''






print()
print('*****  start section 8 - using random and converting to list ********')
print()
import random

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)

print(phonebook[random_key])


print()
print('*****  end section 8 ********')
print()







