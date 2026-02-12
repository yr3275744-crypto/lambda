#1.
double = lambda n: n *2
print(double(7))

#2.
add = lambda a, b: a + b
print(add(3, 5))

#3.
lambda n: True if n % 2 == 0 else False

#4.
lambda a, b: a if a > b else b

#5.
lambda string: string.capitalize()

#6.
lambda string: True if len(string) > 5 else False

#7.
students = [("Danny", 85), ("Yael", 92), ("Uri", 78), ("Noa", 95)]
# key = lambda tuple: tuple[1]
sorted_students = sorted(students, key = lambda tuple: tuple[1])
print(sorted_students)

#8.
inventory = {"shirt": 45, "pants": 120, "hat": 30, "shoes": 200}
inventory_items = inventory.items()
sorted_inventory = sorted(inventory_items, key = lambda tuple: tuple[1])
print(sorted_inventory)