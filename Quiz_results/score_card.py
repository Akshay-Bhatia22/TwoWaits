from queue import Empty
from Quiz.models import CorrectOption, Quiz, QuizQuestion
from rest_framework.response import Response
from rest_framework import status

from Quiz_results.models import ScoreCard
from Quiz_results.serializers import ScoreCardSerializer

from django.core import serializers

# For single correct questions only

def generate_result(quiz_id, user_id):
    quiz_instance = Quiz.objects.get(id=quiz_id)

    title = quiz_instance
    total_questions = quiz_instance.no_of_question
    try:
        student_result = quiz_instance.attempted_quiz.get(student_id=user_id)
    except:
        return Response({'message':'Quiz not attempted by user'}, status=status.HTTP_400_BAD_REQUEST)
        
    # if student score card is already generated
    if student_result.quiz_result_score.all():
        serialized_data = serializers.serialize('python', student_result.quiz_result_score.all())
        return Response(serialized_data[0]['fields'], status=status.HTTP_200_OK)

    else:    
        answers = student_result.student_quiz_result_id
        attempted = answers.count()

        correct = 0

        for answer in answers.all():
            question_id = answer.question_id.id
            correct_id = CorrectOption.objects.get(question_id=question_id).correct.id
            for marked_answer in answer.marked_answer.all():
                student_option_id = marked_answer.option_id.id
                if student_option_id == correct_id:
                    correct +=1

        wrong=attempted-correct
        total_score = str(correct)+' / '+str(total_questions)

        # CREATE Score card in database
        score_instance = ScoreCard.objects.create(
            quiz_result_score_id=student_result,
            title = title,
            total_questions = total_questions,
            attempted = attempted,
            correct = correct,
            wrong = wrong,
            total_score = total_score
        )
        ls = [score_instance]
        serialized_data = serializers.serialize('python', ls)
        return Response(serialized_data[0]['fields'], status=status.HTTP_201_CREATED)




'''
Title : q = Quiz.objects.get(id=50)
Total question : q.no_of_question
# getting student result
result = q.attempted_quiz.get(student_id=3)
Attempted = result.student_quiz_result_id.count()
# loop through result.student_quiz_result_id.all()
.first().marked_answer.all()
loop through marked_answer

1 ----- .first().option_id.id      # user marked option id
2 ----- result.student_quiz_result.all().first().question_id.id

# get correct option id from the above question id
3 ----- q.question.get(id = above).correct.first().id

if 1 == 3:
    correct
'''