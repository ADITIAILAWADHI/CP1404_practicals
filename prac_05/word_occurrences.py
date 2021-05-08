text = input("Text: ")
word_to_count = {}
for i in text.split():
    if i in word_to_count:
        word_to_count[i] += 1
    else:
        word_to_count[i] = 1

word_to_count_lst = [(word, count) for word, count in word_to_count.items()]
sorted_word_to_count = sorted(word_to_count_lst)

for (word, count) in sorted_word_to_count:
    print("{:10}: {}".format(word, count))
