k, m = map(int, input().split())

lists = []
for i in range(k):
    new_list = list(map(int, input().split()))
    lists.append(new_list[1:])

possible_sums = {0}

for lst in lists:
    list_sum = set()
    for n in lst:
        for s in possible_sums:
            list_sum.add((s + (n**2)) % m)
    possible_sums = list_sum


print(max(possible_sums))
