# For loop
for i in range(6):
    for y in range(6):
        if y<i:
            print("*", end="")
        else:
            print(f"Now y value is  {y} and i value is {i}")

# For loop  break
# The break statement is used inside the loop to exit out of the loop. If the break statement is used inside a nested loop (loop inside another loop), it will terminate the innermost loop.
  for i in range(4):
    for y in range(4):
        if y == i:
            break
       print(f"Now y value is  {y} and i value is {i}")
    
    
# For loop  continue
# The continue statement skip the current iteration and move to the next iteration
for i in range(4):
    for j in range(4):
        if j == i:
            continue
        print(f"Now i value is  {i} and j value is {j}")
        
        
#Single Line Nested Loops Using List Comprehension
first = [2, 3, 4]
second = [20, 30, 40]
final= [ i+j for i in first for j in second]
print(final)

#Single Line Nested Loops Using List Comprehension
first = [2, 3, 4]
second = [20, 30, 40]
for i in first:
    for j in second:
        print(i+j, end=" ")
