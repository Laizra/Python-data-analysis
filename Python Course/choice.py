from Question import Question

question_prompt = [
    "what color is a banana?\n(a) Purple\n(b) Yellow\n(c) Grey\n",
    "What color is an apple?\n(a) Green\n(b) Pink\n(c) Black\n",
    "What color is a grape?\n(a) yellow\n(b) teal\n(c) purple\n",
]

questions = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
