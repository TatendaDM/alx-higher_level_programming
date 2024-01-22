#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    sum_total = 0
    while True:
        try:
            if sum_total < x:
                print (f"{my_list[i]}", end="")
                sum_total += 1
            else: 
                print()
                return sum_total
        except IndexError:
            print()
            return sum_total
