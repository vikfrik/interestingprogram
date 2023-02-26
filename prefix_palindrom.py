def is_palindrom(s):
    if s[:] == s[::-1]:
        return True
    else:
        return False
    
t = int(input())
for i in range(t):
    s = input()
    a = []
    l = 0
    for i in range(len(s), 1, -1):
        if is_palindrom(s[:i]):
            l = 1
            print(i)
            break
    if l != 1:
        print (1)
            



