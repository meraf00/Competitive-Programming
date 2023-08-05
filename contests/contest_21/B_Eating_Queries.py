import bisect

test_cases = int(input())

for _ in range(test_cases):
    n_candies, n_queries = map(int, input().split())

    quantity = list(map(int, input().split()))

    quantity.sort(reverse=True)

    prefix = [i for i in quantity]

    for i in range(1, len(quantity)):
        prefix[i] = prefix[i - 1] + prefix[i]

    answer = []

    for _ in range(n_queries):
        query = int(input())

        if query > prefix[-1]:
            answer.append(str(-1))

        else:
            ans = bisect.bisect_left(prefix, query)
            answer.append(str(ans + 1))


    print("\n".join(answer))
