print('puzzle1-1')

f = open("input1-1.txt","r")
lines = f.readlines()

sum = 0
elf = 0
topsum = 0

for line in lines:
    line = line.replace("\n","")

    if not line.strip():
        print(sum)
        if sum > topsum:
            topsum = sum
            elf += 1
        sum = 0
    else:
        sum = sum + int(line)

print("Top sum = " + str(topsum))
print("Top elf = " + str(elf))

#This is the correct answer
#Top sum = 67633
#Top elf = 2

print(line)






























#    def my_function(*kids):
#  print("The youngest child is " + kids[2])

#my_function("Emil", "Tobias", "Linus") 