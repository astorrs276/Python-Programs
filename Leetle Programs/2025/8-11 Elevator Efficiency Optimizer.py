def solve(current, requests):
    return 0 if requests == [] else min(abs(current - min(requests)), abs(current - max(requests))) + max(requests) - min(requests)