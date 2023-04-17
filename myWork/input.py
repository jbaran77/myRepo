#value = input()

#print(value)

num = int(input("Enter a number"))
num +=1
print("You entered",num)


with open('movies.txt') as file:
    for line in file:
        print(line.strip())


with open('heights.txt') as file:
    for line in file:
        line = line.strip()
        values = line.split()
        print(values)
        fn = values[0]
        ln = values[1]
        height = int(values[2])

        
