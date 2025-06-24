import re
def solve(phone):
    return any([re.match('\(\d{3}\) \d{3}-\d{3}', phone), re.match('\d{3}-\d{3}-\d{3}', phone), re.match('\d{3}\.\d{3}\.\d{3}', phone), re.match('\d{10}', phone)])