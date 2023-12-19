#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lilac = []
    for i in range(list_length):
        try:
            lilac.append(my_list_1[i] / my_list_2[i])
            continue
        except ZeroDivisionError:
            print("division by 0")
            lilac.append(0)
        except TypeError:
            print("wrong type")
            lilac.append(0)
        except IndexError:
            print("out of range")
            lilac.append(0)
        finally:
            pass
    return (lilac)
