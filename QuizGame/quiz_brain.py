# ask questions
# check if the answer was correct
# check if there are any more questions

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self): 
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else: 
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
    
    def end_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score is: {self.score}/{self.question_number}.")