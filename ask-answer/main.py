questions = {
    'Question 1': {
        'question': 'How much is 2 + 2?',
        'answers': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '6',
        },
        'correct_answer': 'b',
    },
    'Question 2': {
        'question': 'How much is 5 * 3?',
        'answers': {
            'a': '4',
            'b': '7',
            'c': '15',
            'd': '60',
        },
        'correct_answer': 'c',
    },
    'Question 3': {
        'question': 'How much is 2 - 6?',
        'answers': {
            'a': '4',
            'b': '-4',
            'c': '15',
            'd': '-7',
        },
        'correct_answer': 'b',
    },
    'Question 4': {
        'question': 'Which is the square root of 25?',
        'answers': {
            'a': '7',
            'b': '10',
            'c': '2',
            'd': '5',
        },
        'correct_answer': 'd',
    },
    'Question 5': {
        'question': 'What is 3 cubed?',
        'answers': {
            'a': '9',
            'b': '36',
            'c': '27',
            'd': '18',
        },
        'correct_answer': 'c',
    },
}

print('{:-^30}'.format(' QUESTIONS '))

correct_answers = 0

for questions_key, questions_value in questions.items():
    print(f'{questions_key}: {questions_value["question"]}')
    for answer_key, answer_value in questions_value['answers'].items():
        print(f'({answer_key}): {answer_value}')

    user_answer = input('Your answer: ')
    if user_answer == questions_value['correct_answer']:
        correct_answers += 1
    else:
        correct_answers = correct_answers
    print()

print('{:-^28}'.format('-'))

questions_quantity = len(questions)
percentage = correct_answers / questions_quantity * 100
print(f'You got {correct_answers} answers right.')
print(f'Your hit percentage was: {percentage}%')
