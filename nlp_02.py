def calculate_edit_distance(source, target):
    len_source = len(source)
    len_target = len(target)
    edit_matrix = []

    for i in range(len_source + 1):
        edit_matrix.append([0] * (len_target + 1))
    
    for i in range(1, len_source + 1):
        edit_matrix[i][0] = edit_matrix[i-1][0] + 1
    for j in range(1, len_target + 1):
        edit_matrix[0][j] = edit_matrix[0][j-1] + 1
    
    for i in range(1, len_source + 1):
        for j in range(1, len_target + 1):
            if source[i-1] == target[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 2

            edit_matrix[i][j] = min(
                edit_matrix[i-1][j] + 1,                  # Deletion
                edit_matrix[i-1][j-1] + substitution_cost, # Substitution
                edit_matrix[i][j-1] + 1                   # Insertion
            )
  
    ## Backtracking to find the aligned strings
    i, j = len_source, len_target
    aligned_source = ""
    aligned_target = ""

    while True:
        if source[i-1] != target[j-1]:
            substitution_cost = 2
        else:
            substitution_cost = 0

        if edit_matrix[i][j] == (edit_matrix[i-1][j-1] + substitution_cost):
            if source[i-1] == target[j-1]:
                aligned_source += source[i-1]
                aligned_target += target[j-1]
            else:
                aligned_source += source[i-1] + '*'  
                aligned_target += "*" + target[j-1]
            i -= 1
            j -= 1
        elif edit_matrix[i][j] == edit_matrix[i-1][j] + 1:
            aligned_source += source[i-1]
            aligned_target += "*"
            i -= 1
        elif edit_matrix[i][j] == edit_matrix[i][j-1] + 1:
            aligned_source += "*"
            aligned_target += target[j-1]
            j -= 1

        if i == 0 and j == 0:
            break

    print(aligned_source[::-1])
    print(aligned_target[::-1])

    return

# Example usage
calculate_edit_distance("pqrpq", "qpprq")

