import pygame

from src.components.game_status import GameStatus
from src.NitzanimGameFoler.QuestionHandler import QuestionHandler_class
from src.NitzanimGameFoler.Question import *
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService


pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    list_questions = QuestionHandler_class.turn_to_list_buttons(Question.parse_csv("C:\\Users\\Owner\\PycharmProjects\\NitzanimGame2\\src\\NitzanimGameFoler\\Question_FIle.csv"))

    while True:
        print(GlobalState.QUESTION_INDEX, " val")
        MusicService.start_background_music()
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase(list_questions)
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()
        elif GlobalState.GAME_STATE == GameStatus.CORRECT_ANSWER:
             main_menu_phase()
        update_game_display()


if __name__ == "__main__":
    main()
