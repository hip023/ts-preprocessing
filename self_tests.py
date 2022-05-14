import hashlib
from typing import Union

# If you got here, answers are hashed :) go and do your homework please :) :)
ANSWERS = {
    "E1": [b'\xccJ\x83)\xfc\xd1]\xf2', b'\x08\x80\x15\xd5\xcb*\\\xf7', b'\xec\xcb\xc8~K\\\xe2\xfe',
           b'\x10\x17\xbf\xd4g9U\xff', b'\xba\xfds"\xc6\xe9}%', b'\x93\xcb\xa0tT\xf0jJ', b'\x9a\x11X\x15M\xfaB\xca',
           b'\xc8\x1er\x8d\x9dL/c', b'n\xa9\xab\x1b\xaa\x0e\xfb\x9e', b'\x08\xed544\x172\x1c'],
    "E3": [b'\x8e\x98\xd8\x1f\x82\x170I', b'_\x95\x14\x0ek\x0b\xd1\xd8', b"\xf0\x0eK'\x85Ro\xd5",
           b'\xc8\x1er\x8d\x9dL/c', b'\xdaO\xb5\xc6\xe9>t\xd3', b'\xdaO\xb5\xc6\xe9>t\xd3',
           b'\xc4\xcaB8\xa0\xb9#\x82', b'\xc4\xcaB8\xa0\xb9#\x82', b'\xb7\xa7\x82t\x1ffr\x01',
           b'\xc8\x1er\x8d\x9dL/c'],
    "E5": [b'\x9e<\xfcH\xec\xcf\x81\xa0', b'\x98\xf17\x08!\x01\x94\xc4', b'\xe9\x89\xa0\xb0p*\x90.',
           b'\xba\xfds"\xc6\xe9}%', b'\xed\xf5\xf1\xdc3m\xb7e', b'\xc8\x1er\x8d\x9dL/c', b'vB=\x83R\xc9\xe8\xfc',
           b'vB=\x83R\xc9\xe8\xfc', b'\xf7ij\x9b6*\xc5\xa5', b'\xc4\xcaB8\xa0\xb9#\x82', b'\x93\xcb\xa0tT\xf0jJ',
           b'\x93\xcb\xa0tT\xf0jJ', b'\x93\xcb\xa0tT\xf0jJ', b'\x93\xcb\xa0tT\xf0jJ']}


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
