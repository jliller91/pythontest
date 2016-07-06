# print("Hello,world")


# str = input("Enter your input: ");
# print("Received input is : ", str)


fo = open("testread.txt", "r+")
fo2 = open("testread2.txt", "r+")


fo2.write(fo.read());

fo.close()
fo2.close()