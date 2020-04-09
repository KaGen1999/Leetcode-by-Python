n = int(input())
for i in range(n):
    s = input()
    b = ''
    new_s = ''
    count = 1
    state = 0
    for each in s:
        if each != b:
            if state == 1:
                new_s = new_s + each
                state = 2
            elif state == 2:
                new_s = new_s + each
                state = 0
            else:
                new_s = new_s + each

        else:
            if state == 0:
                state = 1
                new_s = new_s + each
        b = each

    print(new_s)