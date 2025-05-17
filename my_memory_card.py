
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QPushButton,
    QLabel, QVBoxLayout, QRadioButton,
    QHBoxLayout, QMessageBox, QGroupBox,QButtonGroup)
from random import shuffle, choice
class Question():
    def __init__(self, q, r_a, w_a1, w_a2, w_a3):
        self.question = q
        self.right_answer = r_a
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3


questions = []
questions.append(Question('Куда баскетболист забрасывает мяч?',
                        'в корзину',
                        'в рюкзак',
                        'в миску',
                        'в лунку'))
questions.append(Question('сколько сердец у осьминога?',
                        '3',
                        '4',
                        '2',
                        '8'))
questions.append(Question('какое животное из предложенных откладывает яйца',
                        'утконос',
                        'кенгуру',
                        'корова',
                        'заяц'))
questions.append(Question('Какой город является самым старым морским портом России?',
                        'Архангельск',
                        'Находка',
                        'Мурманск',
                        'Севастополь'))
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    txt.setText(q.question)
    ans.setText(q.right_answer)
    show_question()
def check_answer():
    win.total += 1
    if buttons[0].isChecked():
        anstxt.setText("Правильно")
        show_result()
        win.score += 1
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        anstxt.setText('Неправильно')
        show_result()
    print("Статистика")
    print('Всего вопросов', win.total)
    print('Правильных ответов', win.score)
    print('Рейтинг', win.score/win.total * 100,'%')
def next_question():
    randquestion = choice(questions)
    ask(randquestion)
app = QApplication([])
win = QWidget()
win.total = 0
win.score= 0
win.setWindowTitle("Memory Card")
win.resize(400, 400)
txt = QLabel('вопрос')
btn = QPushButton("Ответить")
RadioGroupBox = QGroupBox('Варианты')
rbtn1 = QRadioButton('вариант1')
rbtn2 = QRadioButton('вариант2')
rbtn3 = QRadioButton('вариант3')
rbtn4 = QRadioButton('вариант4')
buttons =[rbtn1, rbtn2, rbtn3, rbtn4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
AnsGroupBox = QGroupBox("Результат теста")
AnsGroupBox.hide()
v_line4 = QVBoxLayout()
anstxt = QLabel('Правильно/Неправильно')
ans = QLabel('Правильный ответ')

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()

v_line2.addWidget(rbtn1)
v_line2.addWidget(rbtn2)
v_line3.addWidget(rbtn3)
v_line3.addWidget(rbtn4)
h_line4.addLayout(v_line2)
h_line4.addLayout(v_line3)
RadioGroupBox.setLayout(h_line4)
h_line1.addWidget(txt, alignment = Qt.AlignCenter)
h_line2.addWidget(RadioGroupBox)
h_line3.addWidget(btn, alignment = Qt.AlignCenter)
v_line1.addLayout(h_line1)
v_line1.addLayout(h_line2)
v_line1.addLayout(h_line3)
win.setLayout(v_line1)

v_line4.addWidget(anstxt)
v_line4.addWidget(ans, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(v_line4)
h_line2.addWidget(AnsGroupBox)
ask(questions[0])
btn.clicked.connect(start_test)



win.show()
app.exec()