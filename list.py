lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kie", "Levi", "Lisa", "alex", "jay", "stefan"]
friends.insert(1, "Liv")

print(friends[0:])

print(friends[1])
# ----------------------Tuples-------------------------
coordinates = (4, 5)
print(coordinates[0])
# ----------------------Functions-----------------------


def say_hi(name, age):
    print("Hello " + name + " You're " + age)


say_hi("Derek", "19")
say_hi("Steve", "20")
