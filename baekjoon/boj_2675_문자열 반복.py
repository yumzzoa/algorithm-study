#2675

T = int(input())

for s in range(T):
    number, word = input().split()
    for i in range(len(word)):
        print(int(number) * word[i],  end='')
    print()