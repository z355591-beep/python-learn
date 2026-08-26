blocks = int(input("Enter the number of blocks: "))

height = 0
# Write your code here.
while blocks >= (height + 1):
    height += 1
    blocks -= height


print("The height of the pyramid:", height)