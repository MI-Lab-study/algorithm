from math import ceil
from collections import defaultdict


def compute_time(in_time, out_time):
    in_h, in_m = map(int, in_time.split(":"))
    out_h, out_m = map(int, out_time.split(":"))
    t = (out_h * 60 + out_m) - (in_h * 60 + in_m)
    return t


def compute_fee(fees, t):
    a, b, c, d = fees
    fee = b if t <= a else b + ceil((t - a) / c) * d
    return fee


def solution(fees, records):
    result, my_dict = defaultdict(int), dict()
    for record in records:
        time, car, inout = record.split(" ")
        if inout == "IN":
            my_dict[car] = time
        else:
            result[car] += compute_time(my_dict[car], time)
            del my_dict[car]

    for car, time in my_dict.items():
        result[car] += compute_time(time, "23:59")

    return [compute_fee(fees, result[car]) for car in sorted(result)]
