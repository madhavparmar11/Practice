a = (1, 2, 3, 4, 5, 6, 7, 8)
x = int(input("write a number u wanna search: "))
print(type(a))
for items in a:
    print(items)
    
    # searching for a number
    
    if x == items:
        print("found")
        break
    else:
        print("searching...")
