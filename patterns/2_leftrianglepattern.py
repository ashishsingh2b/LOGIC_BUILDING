# rows= int(input("Enter The number of stars: "))

# for i in range(1,rows+1):
#     print(" " * (rows-i) + "*" * i)


# Enter The number of stars: 5
#     *
#    **
#   ***
#  ****
# *****

rows=5

for i in range(1,rows+1):
    print(" " * (rows-i) +  "*" * i)  # This line will throw an error because you are trying to multiply a string

