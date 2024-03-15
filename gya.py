def s(word_list, word, num=0):
    if num >= len(word_list):
        print("Fail")
        return None
    if word == word_list[num]:
        print(num)
        return
    else:
        return s(word_list, word, num + 1)
