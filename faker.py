from Quiz.models import Quiz, QuizQuestion, Option, CorrectOption
from Accounts.models import UserAccount

# CREATING QUIZ 
author = UserAccount.objects.get(id=2)
quiz_obj = Quiz.objects.create(
    author_id=author,
    title="C Programming Quiz",
    description="Basic C Questions",
    no_of_question=5,
    time_limit=15
)
quiz_question = QuizQuestion.objects.create(
    quiz_id = quiz_obj,
    question_text = "What is the size of char data type"
)
for i in range(4):
    option_obj = Option.objects.create(
        question_id = quiz_question,
        option = f"{i+1} byte"
    )
correct = CorrectOption.objects.create(
    question_id = quiz_question,
    correct = option_obj
)