#q1
list1=[]
list2=[]

for i in range(5):
  n=int(input("enter list1 values: "))
  list1.append(n);

for i in range(5):
  n=int(input("enter list2 values: "))
  list2.append(n);
print("\n")
print(list1)
print(list2)

dp=0
for i in range(5):
  dp=list1[i]*list2[i];
print("dot product of these lists are: ",dp);

