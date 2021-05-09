def filter_long_words(words, x):
    result = []
    for i in words:
        if len(i) > x:
            result.append(i)
    return result
