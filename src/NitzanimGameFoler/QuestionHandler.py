from src.NitzanimGameFoler.Button import Button
from src.NitzanimGameFoler.Constants_Buttons import *


class QuestionHandler_class:
    def __init__(self, question):
        self.question_text = question.question_text
        self.rightAns = question.rightAns
        self.buttons = []
        for i in range(4):
            button = Button(question.pos_answers[i], BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_POS_LIST[i], ELEVATION)
            self.buttons.append(button)

    def check_click_screen(self):
        for i, button in enumerate(self.buttons):
            if button.check_click():
                return True
        return False
    def check_answer(self):
        for i, button in enumerate(self.buttons):
            if button.check_click():
                return i + 1 == self.rightAns
        return False

    @staticmethod
    def turn_to_list_buttons(questions):
        list_questions = []
        for question in questions:
            list_questions.append(QuestionHandler_class(question))
        return list_questions

    @staticmethod
    def draw(screen, question) -> None:
        for i in range(4):
            question.buttons[i].draw(screen)