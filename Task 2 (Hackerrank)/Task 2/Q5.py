if _name_ == '_main_':
    n = int(input())
    int_list = [int(i) for i in input().split()]
    int_tuple = tuple(int_list)
    print(hash(int_tuple))