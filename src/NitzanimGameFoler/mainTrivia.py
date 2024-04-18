import pygame
import sys
from src.NitzanimGameFoler.QuestionHandler import QuestionHandler_class
from Question import Question
from Constants_Buttons import *
from Button import *

def mainT():
    list_questions = QuestionHandler_class.turn_to_list_buttons(Question.parse_csv("Question_FIle.csv"))
    current_question_index = 0
    rightAns = 0
    wrongAns = 0

    while True:
        textSurf = Surface(list_questions[current_question_index].question_text, TEXT_SURF_WIDTH, TEXT_SURF_HEIGHT, TEXT_SURF_POS, TEXT_SURF_COLOR, FONT_SIZE_QUESTION, WHITE)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if list_questions[current_question_index].check_answer():
                    print("Correct!")
                    current_question_index += 1
                    rightAns += 1
                else:
                    if list_questions[current_question_index].check_click_screen():
                        print("Incorrect!")
                        current_question_index += 1
                        wrongAns += 1

            if current_question_index >= len(list_questions):
                print(f"Wrong ans: {wrongAns}, right ans: {rightAns}")
                pygame.quit()
                sys.exit()

        screen.fill('#DDF0FB')
        textSurf.draw()
        QuestionHandler_class.draw(screen, list_questions[current_question_index])
        pygame.display.flip()
        clock.tick(60)

mainT()


