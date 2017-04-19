def find_max_min(x):
    min_max = []
    y = sorted(x)
    n =len(y)
    min = y[0]
    max = y[n - 1]
    for i in y:
        if min == max:
            min_max.append(min)
            return min_max
        else:
            min_max.append(min)
            min_max.append(max)
            return min_max
1 Comment Collapse
