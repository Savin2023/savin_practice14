my_list = [0, 2, 5, 6, 8, 10]    

def out_el(x):
    if x<0:
        print("Конец списка")
        return
    print(my_list[x])
    out_el(x-1)

out_el(len(my_list)-1)
