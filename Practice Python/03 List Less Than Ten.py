num = int(input("Choose a number: "))
a = range(num)
new_list = [ ]

for i in a:
    if i < num:
        new_list.append(i)

print(new_list)