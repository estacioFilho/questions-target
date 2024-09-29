variations_letters = ["a","á", "â", "ã"]

def check_existence_latter(number_letter, word):
    if number_letter > 0:
        return f"A palavra '{word}' contém a letra 'a' e se repete {number_letter} vez"
    else:
        return f"A palavra '{word}' não contém a letra 'a'."

def count_latter(word):
    existence_count = 0
    for variations in variations_letters:
        for letter in word.lower():
            if letter == variations:
                existence_count += 1
    sub_result = check_existence_latter(existence_count, word)
    return sub_result

iterated_word = input("Digite uma palavra: ")
result_count = count_latter(iterated_word)
print(result_count)
        
