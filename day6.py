# Enter your code here. Read input from STDIN. Print output to STDOUT
test_cases = int(input())

for _ in range(test_cases):
    s = input()
    print("{0} {1}".format(s[::2], s[1::2]))
