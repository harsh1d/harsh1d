# def function_or_relation(pairs):
#     domain = set()
#     range_map = {}

#     for pair in pairs:
#         domain.add(pair[0])

#         if pair[1] not in range_map:
#             range_map[pair[1]] = 0
#         range_map[pair[1]] += 1

#     for element in domain:
#         if element not in range_map or range_map[element] > 1:
#             return "general relation"

#     return "function"
def function_or_relation(pairs):
    domain = set()
    range_map = {}

    for pair in pairs:
        domain.add(pair[0])

        if pair[1] not in range_map:
            range_map[pair[1]] = 0
        range_map[pair[1]] += 1

    for element in domain:
        if element not in range_map or range_map[element] > 1:
            return "general relation"

    return "function"


def get_input():
    pairs = []
    while True:
        pair = input("Enter a pair (e.g., 'a,b') or 'done' to finish: ")
        if pair.lower() == 'done':
            break
        else:
            pairs.append(tuple(pair.split(',')))
    return pairs


def main():
    pairs = get_input()
    result = function_or_relation(pairs)
    print(f"The input constitutes a {result}.")


if __name__ == "__main__":
    main()