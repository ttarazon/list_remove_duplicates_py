
def build_list_func():
    loop_list = []
    start_count_var = 0
    print("The purpose of this program is to create a list based on length, then remove duplicates.")
    list_quant_var = input("How many digits do you want in your list : ")
    while int(start_count_var) < int(list_quant_var):
       digit_var = input("Enter a digit: ")
       loop_list.append(digit_var)
       start_count_var += 1
    else:
        remove_dup_func(loop_list)


def remove_dup_func(loop_list):
    loop_list = set(loop_list)
    loop_list = list(loop_list)
    loop_list.sort()
    print(loop_list)


build_list_func()







