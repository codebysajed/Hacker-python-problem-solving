def minion(word):
    vawel = ["a", "e", "i", "o", "u"]
    kevin = 0
    stuart = 0

    for i in range(len(word)):
        if word[i] in vawel:
            kevin += (len(word) - i)
        else:
            stuart += (len(word) - i )

    if kevin > stuart:
        print(f'kevin score { kevin}')
    else:
        print(f'stuart score { stuart}')

minion('banana')

    

