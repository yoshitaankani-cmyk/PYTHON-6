
key = input("Enter answer key: ").upper()
answers = input("Enter student answers (- for unanswered): ").upper()

if len(key) != len(answers):
    print("Invalid answer count")

else:
    correct = 0
    wrong = 0
    unanswered = 0

    positive = 4
    negative = 1

    for i in range(len(key)):

        if answers[i] == "-":
            unanswered = unanswered + 1

        elif answers[i] == key[i]:
            correct = correct + 1

        else:
            wrong = wrong + 1

    score = (correct * positive) - (wrong * negative)

    print("\n----- EXAM RESULT -----")
    print("Correct answers:", correct)
    print("Wrong answers:", wrong)
    print("Unanswered questions:", unanswered)
    print("Final score:", score)
