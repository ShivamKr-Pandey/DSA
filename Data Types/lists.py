x = ["Now", "we", "are", "cooking!"]
# print(type(x))
# print(x, end=" ")
len(x)


fruits = ["Pineapple", "Apple", "Banana", "Mango"]

# Append
fruits.append("Kiwi")

# Insert
fruits.insert(1,"Orange")

# Remove
fruits.remove("Apple")

# Pop
fruits.pop(4) 
# print(fruits)


# Iterating over Lists

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

# print("Total chanracters: {}, Average length: {}".format(chars, chars/len(animals)))


# List from Tuples 
def full_emails(people):
    results = []
    for email, name in people:
        results.append("{} <{}>".format(name, email))
    return results
    
new_list = [("alex@email.com", "Alex Diego"), ("shay@example.com", "Shay Com"), ("shami@dummy.com", "Sam Chusu")]

# print(full_emails(new_list))


# List Comprehension 

multiples = []
for x in range(1,11):
    multiples.append(x*7)

# print(multiples)

# Now with LC :- 
multiples = [x*7 for x in range(1,11)]
# print(multiples)

#######################################

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]

# print(lengths)

# Now with LC with conditions :-
z = [x for x in range(0,101) if x % 3 == 0]
print(z)