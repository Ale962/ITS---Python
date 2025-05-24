# Optional Exercise 4

'''
4. Text Analysis:

    Create a function that takes a paragraph and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.


'''

def WordsCounter(text: str) -> None:
    
    words_repetition: dict = {}
    words_list = text.split()
    

    for x in words_list:
        if x not in words_repetition.keys():
            words_repetition[x] = 1
        else:
            words_repetition[x] += 1

    v_list = []
    for v in words_repetition.values():
        v_list.append(v)

    v_max = max(v_list)
    k_max = " ".join([key for key, val in words_repetition.items() if val == v_max])
    print(f"The most frequent words is/are {k_max} with {v_max} repitions")


if __name__ == "__main__":
    text = "Create a function that takes a paragraph and counts the number of occurrences of each word.The function should print a report showing the most frequent words and their number of occurrences.You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences."

    WordsCounter(text)