import random

words = ['destructuring', 'love', 'death', 'chicken', 'yellow', 'red', 'fireplace', 'desire', 'workshop', 'mess',
         'arrangement', 'emotion', 'concept']
secret = random.choice(words)
typed = []
definitive_typed = []
chances = 3

while True:
    if chances == 0:
        print('You lose!!!')
        break

    letter = input('Type one letter: ').lower()

    if not letter.isalpha():
        print('What? Type a letter')
        continue

    if len(letter) > 1:
        print('Type only ONE letter')
        continue

    if letter in definitive_typed:
        print('You already said this letter, use another letter')
        continue

    typed.append(letter)
    definitive_typed.extend(typed)

    if letter in secret:
        print(f'Wow! Letter "{letter}" exist in the secret word :o')
    else:
        print(f"This letter don't exist in the secret word :(")
        typed.pop()
        chances -= 1

    temporary_secret = ''
    for secret_letter in secret:
        if secret_letter in typed:
            temporary_secret += secret_letter
        else:
            temporary_secret += '*'

    if temporary_secret == secret:
        print(f'Congratulations, you win! The secret word was "{temporary_secret}"')
        break
    else:
        print(f'CHANCES: {chances}')
        print(f'{temporary_secret}')

    print()
