from pandas import DataFrame
def diagonals(n):

    rows = []
    for i in range(n):

        cols = []

        for j in range(n):

            cols.append(i+j)

        rows.append(cols)

    return rows

x = DataFrame(diagonals(4))
print(x)