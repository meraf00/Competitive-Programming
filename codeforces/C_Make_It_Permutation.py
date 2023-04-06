def make_permutation_cost(nums, del_cost, ins_cost):
    total_cost = 0

    nums.sort()

    if nums[0] == 1:
        unique = [nums[0]]
    else:
        # cost to insert 1
        total_cost += ins_cost
        unique = [1, nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != unique[-1]:
            unique.append(nums[i])
        else:
            # cost to remove duplicates
            total_cost += del_cost

    best_cost = total_cost + del_cost * (len(unique) - 1)

    for i in range(1, len(unique)):
        if unique[i] - unique[i - 1] != 1:
            insertion_cost = ins_cost * (unique[i] - unique[i - 1] - 1)

            total_cost += insertion_cost

        deletion_cost = del_cost * (len(unique) - i - 1)

        best_cost = min(total_cost + deletion_cost, best_cost)

    return best_cost


test_cases = int(input())

for _ in range(test_cases):
    n, deletion_cost, insertion_cost = map(int, input().split())

    nums = list(map(int, input().split()))

    print(make_permutation_cost(nums, deletion_cost, insertion_cost))
