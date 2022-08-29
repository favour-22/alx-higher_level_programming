integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for i in my_list[1:]:
        if max_val < i:
            max_val = i
    return 
