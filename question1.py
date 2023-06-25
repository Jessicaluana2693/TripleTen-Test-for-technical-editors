oldList = []

val = input("Insira um valor: ")

oldList.append(val)
while val:
    val = input("Insira um valor: ")
    if val:
        oldList.append(val)

newList = []


val = len(oldList)-1
for i in range(0, len(oldList)):
    newList.append(oldList[val])
    val -= 1


print(oldList)
print(newList)