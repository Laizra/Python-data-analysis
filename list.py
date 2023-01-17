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


def cube(num):
    return num*num*num


result = cube(4)
print(result)
# ----------------------if statements------------------------
is_blue = False
is_pink = True

if is_blue and is_pink:
    print("is blue and pink")
elif is_blue and not (is_pink):
    print("is blue but not pink")
elif not (is_blue) and is_pink:
    print("is not blue but is pink")
else:
    print("not blue nor pink")
