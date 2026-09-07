def safe_print_list(my_list=[], x=0):
    try:
        print(my_list[x], end="")
    except:
        print("Index out of bounds")
        