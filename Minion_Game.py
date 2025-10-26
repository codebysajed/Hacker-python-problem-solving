def minion(word):
    vowels = ["a", "e", "i", "o", "u"]
    kevin_score = 0
    stuart_score = 0

    for i in range(len(word)):
        if word[i] in vowels:
            kevin_score += (len(word) - i)
        else:
            stuart += (len(word) - i )

    if kevin_score > stuart_score:
        print(f'kevin score { kevin_score}')
    elif stuart_score > kevin_score:
        print(f'stuart score { stuart_score}')
    else:
        print('Drow')

minion('banana')

    

