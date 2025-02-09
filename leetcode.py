def mesclar_strings(word1, word2):
    resultado = ''.join(a + b for a, b in zip(word1, word2))
    return resultado

word1 = "abc"
word2 = "pqr"
print(mesclar_strings('word1, = word2,'))
