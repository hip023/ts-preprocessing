

def test_e1_01(daily_comments_75, missing_views):
    grade = 0

    to_test = int(daily_comments_75)

    if to_test == 405:
        grade = grade + 50

    to_test_2 = int(missing_views)

    if to_test_2 == 0:
        grade = grade + 50

    if grade == 100:
        print("YOU ROCKSTAR!! 100 it is :) ")
    elif grade == 50:
        print("Your grade: 50. Try again!")
    else:
        print("Sorry. your grade is 0. Try again!")