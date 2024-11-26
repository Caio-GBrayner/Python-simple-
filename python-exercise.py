import re

def count_unique_words(text):
    text = text.lower()
    
    text = re.sub(r'[^\w\s]', '', text)
    
    words = text.split()
    
    unique_words = set(words)
    
    unique_word_count = len(unique_words)
    
    return unique_word_count

user_input = input("Digite um texto: ")

result = count_unique_words(user_input)

print(f"Existem {result} palavras únicas no texto.")