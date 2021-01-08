hello_file = open("hello.txt", "w")
ga_intro = "Hello to all of my GA family"
hello_file.write(ga_intro)
#print(hello_file.read())

hello_file.close()

car_file=open("car.txt", 'w')
new_car_list = 'Tesla Model S\nMercedes C300\nToyota Camry'
car_file.write(new_car_list)
#print(car_file.read())
car_file.close()

#create a file
my_new_file = open('person.txt', 'w')
my_new_file.write('Felix Muwanguzi')
my_new_file.close()

# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

# with open('person.txt', 'w') as person_file:
#     person_file.write('Pete')

#append to a file
# with open('person.txt', 'a') as person_file:
#     person_file.write('\nMike\nDexter')

# with open('person.txt') as people:
#     people_list = (people.readlines())

#     for each_person in people_list:
#         print(each_person)

# with open('person.txt', 'r+') as person_file:
#     print(person_file.read())
#     person_file.write('\nYvonne')
#     print(person_file.read())

#prime numbers multiply each by 2 

def multi(num):
    return num * 2

with open('prime_numbers.txt') as prime_numebers_file:
    prime_numbers = prime_numebers_file.readlines()
    for num in prime_numbers:
        print(multi(int(num)))

# one_to_hundred iterate through the elements in the file and return a list (array) of all the elements that include the word Five or Fifteen
with open('one_to_hundred.txt') as numbers_file:
    list_of_numbers = numbers_file.readlines()
    result = []

    for num_txt in list_of_numbers:
        if 'Five' in num_txt:
            remove_newline_txt = num_txt[:-1]
            result.append(remove_newline_txt)
        elif 'Fifteen' in num_txt:
            remove_newline_txt = num_txt[:-1]
            result.append(remove_newline_txt)
    print(result)