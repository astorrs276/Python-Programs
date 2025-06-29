def solve(ip):
    return (len(ip.split(".")) == 4 and all([0 <= int(num) <= 255 for num in ip.split(".")])) and all([len(str(int(num))) == len(num) for num in ip.split(".")])