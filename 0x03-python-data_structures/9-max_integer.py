def max_integer(my_list=[]):
    ln = len(my_list)
    bg = 0
    if ln >= 1:
        for i in my_list:
            if i > bg:
                bg = i
        return bg
    else:
        return None
