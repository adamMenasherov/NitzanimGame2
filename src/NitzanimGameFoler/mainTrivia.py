import pygame
import sys
from src.NitzanimGameFoler.QuestionHandler import QuestionHandler_class
from src.NitzanimGameFoler.Constants_Buttons import *
from src.global_state import GlobalState
from src.NitzanimGameFoler.Button import Surface, screen, clock

def mainTrivia(list_questions) -> bool:
    if list_questions:
        question = list_questions[GlobalState.QUESTION_INDEX]

        while True:
            textSurf = Surface(question.question_text, TEXT_SURF_WIDTH, TEXT_SURF_HEIGHT, TEXT_SURF_POS, TEXT_SURF_COLOR, FONT_SIZE_QUESTION, WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    answer = question.check_answer()
                    if answer:
                        GlobalState.QUESTION_INDEX += 1
                        return True
                    else:
                        if question.check_click_screen():
                            GlobalState.QUESTION_INDEX += 1
                            return False

                if not list_questions:
                    pygame.quit()
                    sys.exit()

            screen.fill('#DDF0FB')
            textSurf.draw()
            QuestionHandler_class.draw(screen, question)
            pygame.display.flip()
            clock.tick(60)



