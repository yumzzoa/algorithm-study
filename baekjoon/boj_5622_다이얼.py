#5622

Alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

sum = 0

for i in range(len(word)):
    for j in Alphabet:
        if word[i] in j:
            sum = sum + Alphabet.index(j) + 3
print(sum)
