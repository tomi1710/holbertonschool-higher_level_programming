#!/usr/bin/python3
""" Test function find_peak """


def find_peak(int_list):
    """ Finding the peak of a list """
    """ Board cases """
    # middle_point = len(integer_list)/2
    # print (middle_point)

    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list[0]
    if len(int_list) == 2:
        return max(int_list)

    """if len(int_list) % 2 == 0:
        mid_point = int(len(int_list)/2)
    else:
        mid_point = int((len(int_list) - 1)/2)"""

    mid_point = int(len(int_list)/2)
    # print("PUNTO MEDIO: {}".format(middle_point))
    middle = int_list[mid_point]
    # next_int = integer_list[middle_point + 1]
    # prev_int = integer_list[middle_point - 1]
    # first_half = integer_list[:middle_point]
    # print("PRIMERA MITAD {}".format(first_half))
    # second_half = integer_list[middle_point + 1:]
    # print("SEGUNDA MITAD {}".format(second_half))

    if middle > int_list[mid_point - 1] and middle > int_list[mid_point + 1]:
        return middle
    elif middle < int_list[mid_point - 1]:
        return find_peak(int_list[:mid_point])
    else:
        return find_peak(int_list[mid_point + 1:])