paths = []
def solve(begin_word, end_word, word_list):
    def check(word, remaining, path):
        global paths
        path.append(word)
        if word == end_word:
            paths.append(len(path))
            return
        for i in range(len(remaining)):
            word_listed = list(word)
            item_listed = list(remaining[i])
            if len(word_listed) == len(item_listed) and sum([1 if word_listed[i] != item_listed[i] else 0 for i in range(len(word_listed))]) == 1:
                check(remaining[i], remaining[:i] + remaining[i + 1:], path[:])
    check(begin_word, word_list, [])
    return 0 if paths == [] else min(paths)