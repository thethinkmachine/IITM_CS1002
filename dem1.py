import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

with open('dataset.txt', 'r', encoding='utf-8') as file:
    text_data = file.read()

tokens = word_tokenize(text_data)
matrix = {}
for i in range(len(tokens) - 1):
    curr_word = tokens[i]
    next_word = tokens[i + 1]
    if curr_word not in matrix:
        matrix[curr_word] = {}
    if next_word not in matrix[curr_word]:
        matrix[curr_word][next_word] = 0
    matrix[curr_word][next_word] += 1


def answer_question(question):
    tokens = word_tokenize(question)
    if tokens[0] not in matrix:
        return 'Beyond scope of training data!'

    generated_text = ""
    curr_word = tokens[0]
    for i in range(30):
        generated_text += curr_word + " "
        if curr_word not in matrix:
            break
        next_word_probs = matrix[curr_word]
        total_count = sum(next_word_probs.values())
        next_word_cumprobs = [sum(next_word_probs[w] for w in next_word_probs.keys() if w <= word) / total_count for
                              word in sorted(next_word_probs.keys())]
        rand = random.random()
        for j, p in enumerate(next_word_cumprobs):
            if rand < p:
                curr_word = sorted(next_word_probs.keys())[j]
                break

    return generated_text


# Example usage
question = input('Prompt: ')
answer = answer_question(question)
print(answer)  # prints "Beyond scope of training data!" if "What" is not in the training data
