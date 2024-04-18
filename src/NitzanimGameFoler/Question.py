import csv
class Question:
    def __init__(self, question_text, pos_answers, rightAns):
        self.question_text = question_text
        self.pos_answers = pos_answers
        self.rightAns = rightAns

    @staticmethod
    def parse_csv(file_path):
        questions = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                question_text = row[0]
                pos_answers = row[1].split(',')
                right_ans = int(row[2])  # Assuming the index of correct answer starts from 0
                question = Question(question_text, pos_answers, right_ans)
                questions.append(question)
        return questions
