mat = [[1, 2, 3], [4, 5, 6]]
def col_sums(mat):
    result = []
    max_length_row = max([len(row) for row in mat])

    try:
        for i in range(max_length_row):
            count = 0
            for row in mat:
                count += row[i]
            result.append(count)
    except:
        raise ValueError("рваная")
    return result
print(col_sums(mat))