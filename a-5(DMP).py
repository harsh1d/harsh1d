# #WITHOUT USER
# import numpy as np

# def check_relation(pairs):
#     # Converting list of tuples into set for removing duplicate entries
#     pairs = set(pairs)

#     # Initializing set to keep track of unique elements in the first column
#     first_column_set = set()

#     # Iterating through the set of pairs to find unique elements in the first column
#     for pair in pairs:
#         first_column_set.add(pair[0])

#     # Iterating through the set of pairs to find unique elements in the second column
#     second_column_set = set()
#     for pair in pairs:
#         second_column_set.add(pair[1])

#     # If there are more unique elements in the second column than in the first column, it's not a valid relation
#     if len(second_column_set) > len(first_column_set):
#         return False

#     # Converting set of unique elements into list
#     first_column_list = list(first_column_set)
#     second_column_list = list(second_column_set)

#     # Initializing an empty matrix for relation representation
#     relation_matrix = np.zeros((len(first_column_list), len(second_column_list)))

#     # Filling the matrix with values based on the input pairs
#     for pair in pairs:
#         first_index = first_column_list.index(pair[0])
#         second_index = second_column_list.index(pair[1])
#         relation_matrix[first_index][second_index] = 1

#     return relation_matrix


# def main():
#     pairs = [('a', 'b'), ('b', 'c'), ('c', 'd')]
#     relation_matrix = check_relation(pairs)
#     if relation_matrix:
#         print("The input constitutes a valid relation.")
#         print("Matrix representation: ")
#         print(relation_matrix)
#     else:
#         print("The input does not constitute a valid relation.")


# if __name__ == "__main__":
#     main()
import numpy as np

def check_relation(pairs):
    # Converting list of tuples into set for removing duplicate entries
    pairs = set(pairs)

    # Initializing set to keep track of unique elements in the first column
    first_column_set = set()

    # Iterating through the set of pairs to find unique elements in the first column
    for pair in pairs:
        first_column_set.add(pair[0])

    # Iterating through the set of pairs to find unique elements in the second column
    second_column_set = set()
    for pair in pairs:
        second_column_set.add(pair[1])

    # If there are more unique elements in the second column than in the first column, it's not a valid relation
    if len(second_column_set) > len(first_column_set):
        return False

    # Converting set of unique elements into list
    first_column_list = list(first_column_set)
    second_column_list = list(second_column_set)

    # Initializing an empty matrix for relation representation
    relation_matrix = np.zeros((len(first_column_list), len(second_column_list)))

    # Filling the matrix with values based on the input pairs
    for pair in pairs:
        first_index = first_column_list.index(pair[0])
        second_index = second_column_list.index(pair[1])
        relation_matrix[first_index][second_index] = 1

    return relation_matrix


def main():
    # Replace the pairs variable with the result of your input function
    pairs = [('a', 'b'), ('b', 'c'), ('c', 'd')]
    relation_matrix = check_relation(pairs)
    if relation_matrix:
        print("The input constitutes a valid relation.")
        print("Matrix representation: ")
        print(relation_matrix)
    else:
        print("The input does not constitute a valid relation.")


if __name__ == "__main__":
    main()