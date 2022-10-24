items = list(map(int,input("Enter list: ").split()))
x, y = map(int,input("Enter x and y: ").split())
items[0],items[-1]= items[-1], items[0]
print("Sum: ",sum(items)/len(items))

print("Result:", end=" ")
for i in items:
  result = y if i == x else i
  print(result,end=" ")

print("\n Sorted: ", *sorted(items))