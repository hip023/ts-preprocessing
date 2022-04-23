

def test_e1_01(daily_comments_75, missing_views):
    grade = 0

    to_test = int(daily_comments_75)

    if str(hash(str(to_test)))[:8] == '-8755428':
        grade = grade + 50

    to_test_2 = int(missing_views)

    if str(hash(str(to_test_2)))[:8] == '75683047':
        grade = grade + 50

    if grade == 100:
        print("YOU ROCKSTAR!! 100 it is :) ")
    elif grade == 50:
        print("Your grade: 50. Try again!")
    else:
        print("Sorry. your grade is 0. Try again!")

