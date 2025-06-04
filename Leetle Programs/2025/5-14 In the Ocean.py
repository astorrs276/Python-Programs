def solve(coord):
    a = 1 if coord[1] == "0" else 2
    b = 1 if coord[2 + a] == "0" else 2
    return ((coord[0] == "N" or coord[0] == "S") and (0 <= int(coord[1:1 + a]) <= 90) and (coord[1 + a] == "E" or coord[1 + a] == "W") and (0 <= int(coord[2 + a:2 + a + b]) <= 180))