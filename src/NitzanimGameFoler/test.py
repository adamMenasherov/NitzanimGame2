import pygame, sys
from Constants_Buttons import *
from Question import Question
from Button import Button

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)


class Surface:
    def __init__(self, text, width, height, pos, color, font_size, font_color):
        self.text = text
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color
        self.font_size = font_size
        self.font_color = font_color

        self.update_text(text)

    def update_text(self, text):
        self.text = text
        self.render_text()

    def render_text(self):
        lines = []
        words = self.text.split()
        current_line = ''
        font = pygame.font.Font(None, self.font_size)
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] < self.width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)

        rendered_lines = [font.render(line, True, self.font_color) for line in lines]
        self.text_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        y = 0
        for line_surf in rendered_lines:
            self.text_surf.blit(line_surf, (0, y))
            y += line_surf.get_height()

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos[0], self.pos[1], self.width, self.height), border_radius=12)
        screen.blit(self.text_surf, self.pos)



class Question_Handler:
    def __init__(self, question):
        self.question_text = question.question_text
        self.rightAns = question.rightAns
        self.buttons = []
        for i in range(4):
            button = Button(question.pos_answers[i], BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_POS_LIST[i], ELEVATION)
            self.buttons.append(button)

    def check_answer(self):
        for i, button in enumerate(self.buttons):
            if button.check_click():
                return i + 1 == self.rightAns
        return False

    @staticmethod
    def turn_to_list_buttons(questions):
        list_questions = []
        for question in questions:
            list_questions.append(Question_Handler(question))
        return list_questions

    @staticmethod
    def draw(screen, question) -> None:
        for i in range(4):
            question.buttons[i].draw(screen)



def main():
    list_questions = Question_Handler.turn_to_list_buttons(Question.parse_csv("Question_FIle.csv"))
    current_question_index = 0
    rightAns = 0
    wrongAns = 0

    while True:
        global rightAnsSurf
        textSurf = Surface(list_questions[current_question_index].question_text, TEXT_SURF_WIDTH, TEXT_SURF_HEIGHT, TEXT_SURF_POS, TEXT_SURF_COLOR, FONT_SIZE_QUESTION, WHITE)

        for event in pygame.event.get():
            rightAnsSurf = Surface(f"Right Ans: {rightAns}", 150, 50, RIGHT_ANS_POS, "#38761d", 25, BLACK)

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
        rightAnsSurf.draw()
        Question_Handler.draw(screen, list_questions[current_question_index])
        pygame.display.flip()
        clock.tick(60)


main()


