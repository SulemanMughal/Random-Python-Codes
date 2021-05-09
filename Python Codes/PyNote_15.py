def longest_word(words):
    longest = words[0]
    for i in words:
        if len(i) >= len(longest):
            longest = i

    return longest
