# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}
for _ in range(n):
    name, phone_num = input().split(" ")
    phone_book[name] = phone_num

try:
    while True:
        name = input()
        if name not in phone_book.keys():
            print("Not found")
        else:
            print("{0}={1}".format(name, phone_book[name]))

except EOFError:
    pass
