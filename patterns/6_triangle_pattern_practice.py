#1
rows=5

for i in range(1,rows+1):
    print("*" * i)

# *
# **
# ***
# ****
# *****    

#2

rows=5

for i in range(1,rows+1):
    print(" " * (rows-i) +"*" * i)


#3

rows=5
for i in range(rows,0,-1):
    print("*" * i)

#4
rows=5

for i in range(rows,0,-1):
    print(" " * (rows-i) +"*" * i)



