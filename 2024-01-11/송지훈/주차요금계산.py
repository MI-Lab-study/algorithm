def solution(fees, records):
    from collections import defaultdict
    import math

    def calc(s, e):
        in_h, in_m = map(int, s.split(':'))
        out_h, out_m = map(int, e.split(':'))

        return (out_h*60+out_m)-(in_h*60+in_m)

    record_dict = defaultdict(list)

    result_fees = []

    for i in range(len(records)):
        r = records[i].split(' ')
        record_dict[r[1]].append(r[0])

    # in out dictionary 분리하는게 좋아보임

    for key in sorted(record_dict.keys()):
        l = len(record_dict[key])
        s = 0
        times = 0

        if l%2 != 0:
            record_dict[key].append('23:59')


        for j in range((l+1)//2):
            times += calc(record_dict[key][2*j], record_dict[key][2*j+1])

        if times < fees[0]:
            result_fees.append(fees[1])
        else:
            result_fees.append(fees[1]+math.ceil((times-fees[0])/fees[2])*fees[3])

    return result_fees