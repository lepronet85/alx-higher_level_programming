#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            division_result = 0
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] != 0:
                    division_result = my_list_1[i] / my_list_2[i]
                else:
                    raise ZeroDivisionError("division by 0")
            else:
                raise TypeError("wrong type")
        except ZeroDivisionError as zde:
            print(zde)
            new_list.append(division_result)
        except TypeError as te:
            print(te)
            new_list.append(division_result)
        except IndexError as ie:
            print(ie)
            new_list.append(division_result)
        finally:
            pass

    return new_list
