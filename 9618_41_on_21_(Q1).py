def unknown(x,y):
    if x < y:
        print(str(x + y))
        return int(unknown(x + 1, y)*2)
    else:
        if x == y:
            return 1
        else:
            print(str(x + y))
            return int(unknown(x - 1, y)//2)

print("10 and 15") 
print(str(unknown(10, 15))) 
print("10 and 10") 
print(str(unknown(10, 10))) 
print("15 and 10") 
print(str(unknown(15, 10)))
