#Nim game 

win = False;
xor = 0
exception = 0
heap = input("Please enter the size of the heap: ")
while (int(heap) <= 0):
    heap = input("PLease eneter a number greater than 0: ")
arr = []
for x in range(0, int(heap)):
    sticks = input("Enter the number of sticks in heap " + str(x+1) + ": ")
    arr.append(int(sticks))
for stick in list(arr):
    xor = xor ^ stick
    exception = exception + stick
print(arr)
if (xor != 0):
    win = True
if (exception == 1):
    win = False
if (win == False):
    print("This is a losing hand!")
else:
    print("This is a winning hand!")

