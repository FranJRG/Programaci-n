A=True
B=True
print((A or B) and not(A))
print(not (A or B) and B)
print(A or not (B))
print(not ((A and B) and (B or A)))
print("-------------")
A=True
B=False
print((A or B) and not(A))
print(not (A or B) and B)
print(A or not (B))
print(not ((A and B) and (B or A)))
print("---------------")
A=False
B=True
print((A or B) and not(A))
print(not (A or B) and B)
print(A or not (B))
print(not ((A and B) and (B or A)))
print("---------------")
A=False
B=False
print((A or B) and not(A))
print(not (A or B) and B)
print(A or not (B))
print(not ((A and B) and (B or A)))
