# For loop
for i in range(6):
    for y in range(6):
        if y<i:
            print("*", end="")
        else:
            print(f"Now y value is  {y} and i value is {i}")
