def solve(word1, word2, words):
    return min([min([abs(i - j) if words[j] == word2 else float('inf') for j in range(len(words))]) if words[i] == word1 else float('inf') for i in range(len(words))])