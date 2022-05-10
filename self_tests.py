import hashlib
from typing import Union

# If you got here, answers are hashed :) go and do your homework please :) :)
ANSWERS = {
    "E1": [b'\xec\x89Vcz\x99x{', b'\x08\x80\x15\xd5\xcb*\\\xf7', b'\x10\x17\xbf\xd4g9U\xff', b'\xba\xfds"\xc6\xe9}%',
           b'\x93\xcb\xa0tT\xf0jJ', b'\xd8,\x8d\x16\x19\xad\x81v', b'\xc8\x1er\x8d\x9dL/c', b'\x8e)j\x06z7V3',
           b'\x08\xed544\x172\x1c']
}


def get_hash(s: Union[str, int]):
    if not isinstance(s, str):
        s = str(s)
    return hashlib.md5(s.encode()).digest()[:8]


def test_your_notebook(notebook, *args):
    if notebook not in ANSWERS.keys():
        print("Nice try, smarty! Go and Break someone else's code :) ")
        raise ValueError("YOUR GRADE: 0! ")

    answers = ANSWERS.get(notebook)
    response_hash = [get_hash(a) for a in args]
    correct_answers = [answers[i] == response_hash[i] for i, _ in enumerate(answers)]

    grade = int(100 * sum(correct_answers) / len(correct_answers))

    if grade > 93:
        print(f"You Rockstar! That's an A! Your Final Grade: {grade}")
    elif grade > 85:
        print(f"Not Bad! Your Final Grade: {grade}")
    elif grade > 75:
        print(f"Nice try, I bet you can do better next time! Your grade: {grade}")
    else:
        print(f"We're addicted to excellence here... how about you try again? Your grade: {grade}")

    print("-------------")
    print("Grade analysis:")

    for i, _ in enumerate(answers):
        print(f"{args[i]} - {correct_answers[i]}")
