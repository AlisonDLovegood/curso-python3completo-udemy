word = "serenity"
hidden_word = list("*"*len(word))

attempts = 0
print("="*50)
print(f"{'HIDDEN WORD GAME':-^50}")

while True:
    if "*" in hidden_word:
        hidden_word_str = ''.join(hidden_word)
        letter = input("Digite uma letra: ")

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            hidden_word_str = ''.join(hidden_word)
            print(f'- CORRECT: {hidden_word_str}')
        else:
            print(f'- INCORRECT: {hidden_word_str}')
        
        attempts += 1
        print(f'- ATTEMPT(s): {attempts}')
    else:
        print(f"{'GAME OVER!':-^50}\n")
        break