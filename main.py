import json

from random import shuffle

QUIZ_NUMBER = 8
QUIZ_QUESTION_NUMBER = 5
ANSWER_CHOICES = "abcd"

with open("questions.json") as questions_file:
    questions = json.load(questions_file)


for i in range(1, QUIZ_NUMBER+1):
    filename = "Quiz{i}.txt".format(i=i)
    answer_filename = "Quiz{i}-key.txt".format(i=i)
    shuffle(questions)
    quiz_questions = questions[0:5:1]
    right_answers = []
    with open(filename, 'w') as quiz_file:
        for q, question in enumerate(quiz_questions):
            quiz_file.write("{q}) ".format(q=q+1))
            quiz_file.write(question['question_text'])
            quiz_file.write("\n")
            answers = question["wrong_answers"] + [question["right_answer"]]
            shuffle(answers)

            for j, answer in enumerate(answers):

                if answer == question['right_answer']:
                    right_answers.append((q+1, ANSWER_CHOICES[j]))
                quiz_file.write(
                    "{letter}) {answer}    ".format(
                        letter=ANSWER_CHOICES[j],
                        answer=answer)
                )
            quiz_file.write('\n\n')

    with open(answer_filename, 'w') as key_file:
        for pair in right_answers:
            key_file.write(
                "{question_number}-{answer_letter}".format(
                    question_number=pair[0],
                    answer_letter=pair[1]
                )
            )
            key_file.write('\n')
