def modify_list(*l):
    modify_list = []
    for x in l:
        if x % 2 == 0:
            modify_list.append(x // 2)

