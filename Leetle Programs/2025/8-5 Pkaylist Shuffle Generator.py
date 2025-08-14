def solve(songs):
    n = len(songs)
    if n <= 1:
        return list(range(n))

    by_artist = {}
    counts = {}
    for i, (_, artist) in enumerate(songs):
        by_artist.setdefault(artist, []).append(i)
        counts[artist] = counts.get(artist, 0) + 1

    if max(counts.values()) > (n + 1) // 2:
        return []

    order = []
    last_artist = None

    for lst in by_artist.values():
        pass

    for _ in range(n):
        best_artist = None
        best_count = -1
        for a, c in counts.items():
            if a != last_artist and c > best_count:
                best_artist, best_count = a, c

        if best_artist is None or best_count == 0:
            return []

        idx = by_artist[best_artist].pop()
        counts[best_artist] -= 1
        order.append(idx)
        last_artist = best_artist

    return order