'6'
def chunked(s, n):
    words = s.split()
    chunks = [words[i:i+n] for i in range(0, len(words), n)]
    return chunks
s = input()
n = int(input())
print(chunked(s, n))


'7'
def sublists(s):
    words = s.split()
    sublists = [[]]
    for i in range(len(words) + 1):
        for j in range(i + 1, len(words) + 1):
            sublists.append(words[i:j])
    return sublists
s = input()
print(sublists(s))


'8'
def print_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(input())
        matrix.append(row)
    for row in matrix:
        print(' '.join(row))
n = int(input())
m = int(input())
print_matrix(n, m)
