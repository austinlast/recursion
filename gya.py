def s(word_list, word, num=0):
    if word == word_list[num]:
        print(num)
        return
    elif word < word_list[num]:
        print("Fail")
        return
    else:
        return s(word_list, word, num + 1)
