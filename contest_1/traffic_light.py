"""https://codeforces.com/gym/418150/problem/E"""


def min_time_to_cross(current_light, lights):
    if current_light == "g":
        return 0

    stack = []
    distances = [0] * len(lights)
    for i, light in enumerate(lights):
        if light == "g":
            while stack:
                current_light_index = stack.pop()
                distances[current_light_index] = i - current_light_index

        if light == current_light:
            stack.append(i)

    while stack:
        current_light_index = stack.pop()
        first_green = lights.index("g")
        distances[current_light_index] = first_green + \
            len(lights) - current_light_index

    return max(distances)


# prepare input
n_tests = int(input())

times = []
for _ in range(n_tests):
    first_line = input().split(" ")

    n = first_line[0]
    current_light = first_line[1]

    lights = input()

    time = min_time_to_cross(current_light, lights)

    times.append(str(time))

output = "\n".join(times)
print(output)
