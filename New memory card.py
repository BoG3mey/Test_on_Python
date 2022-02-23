#Переменные
from errno import EEXIST
from wave import Wave_write
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json 
from random import randint

from cv2 import ROTATE_180
#Окно
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(300,300)
win1=QWidget()
win1.setWindowTitle('Win Window')
notes_win=QWidget()
#Лейауты
main_layout = QVBoxLayout()             #Основной
layout1=QHBoxLayout()                   #текст
layout2=QHBoxLayout()                   #кнопки1
layout3=QHBoxLayout()                   #кнопки2
layout4=QHBoxLayout()                   #ответить
layout5=QVBoxLayout()
layout6=QVBoxLayout()
#Функции
def buttons():
    global r1
    global r2
    global r3
    global r4
    global data
    global aa
    global num
    global ii
    global emp
    global number
    global false
    global true
    global all
    all = true + false
    with open("memcard.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        if all < len(data):
            for aa in data:
                print(aa)
                print(num)
                if aa in num:
                    emp += 1
                else:
                    number += 1
                    num.append(aa)
                    qestbutton.setText(aa)
                    qq = randint(1,4)
                    if qq == 1:
                        radio1.setText(data[aa]['правильно'])
                        radio2.setText(data[aa]['неправильно1'])
                        radio3.setText(data[aa]['неправильно2'])
                        radio4.setText(data[aa]['неправильно3'])
                        r1 = data[aa]['правильно']
                        r2 = data[aa]['неправильно1']
                        r3 = data[aa]['неправильно2']
                        r4 = data[aa]['неправильно3']
                    if qq == 2:
                        radio1.setText(data[aa]['неправильно3'])
                        radio2.setText(data[aa]['правильно'])
                        radio3.setText(data[aa]['неправильно2'])
                        radio4.setText(data[aa]['неправильно1'])
                        r1 = data[aa]['неправильно3']
                        r2 = data[aa]['правильно']
                        r3 = data[aa]['неправильно2']
                        r4 = data[aa]['неправильно1']
                    if qq == 3:
                        radio1.setText(data[aa]['неправильно3'])
                        radio2.setText(data[aa]['неправильно1'])
                        radio3.setText(data[aa]['правильно'])
                        radio4.setText(data[aa]['неправильно2'])
                        r1 = data[aa]['неправильно3']
                        r2 = data[aa]['неправильно1']
                        r3 = data[aa]['правильно']
                        r4 = data[aa]['неправильно2']
                    if qq == 4:
                        radio1.setText(data[aa]['неправильно3'])
                        radio2.setText(data[aa]['неправильно2'])
                        radio3.setText(data[aa]['неправильно1'])
                        radio4.setText(data[aa]['правильно'])
                        r1 = data[aa]['неправильно3']
                        r2 = data[aa]['неправильно2']
                        r3 = data[aa]['неправильно1']
                        r4 = data[aa]['правильно']   
                    break
        else:
            radio1.hide()
            radio2.hide()
            radio3.hide()
            radio4.hide()
            button.hide()
            qestbutton.hide()
            result.show()
            allqest = QLabel('Всего вопросов: ' + str(all))
            tru = QLabel('Правильных ответов: ' + str(true))
            fal = QLabel('Неправильных ответов: ' + str(false))
            layout6.addWidget(allqest)
            layout2.addWidget(tru)
            layout3.addWidget(fal)
def check():
    global true
    global false
    if radio1.isChecked():
        if r1 == data[aa]['правильно']:
            true += 1
            win()
        else:
            false += 1
            lose()
    if radio2.isChecked():
        if r2 == data[aa]['правильно']:
            true += 1
            win()
        else:
            false += 1
            lose()
    if radio3.isChecked():
        if r3 == data[aa]['правильно']:
            true += 1
            win()
        else:
            false += 1
            lose()
    if radio4.isChecked():
        if r4 == data[aa]['правильно']:
            true += 1
            win()
        else:
            false += 1
            lose()
    print(true, false)
def win():
    group_box.hide()
    button.hide()
    qestbutton.hide()
    wintext.show()
    button2.show()
def rec():
    losetext.hide()
    wintext.hide()
    button2.hide()
    group_box.show()
    button.show()
    qestbutton.show()
    buttons()
def lose():
    group_box.hide()
    button.hide()
    qestbutton.hide()
    losetext.show()
    button2.show()
#Что-то
num = []
true = 0
false = 0
ii = 0
number = 0
emp = 0
all = 0
#Обьэкты
result = QLabel('Тест окончен')
group_box = QGroupBox('Варианты ответов')
qestbutton = QLabel('Вопрос')
radio1 = QRadioButton("button 1")
radio2 = QRadioButton("button 2")
radio3 = QRadioButton("button 3")
radio4 = QRadioButton("button 4")
button = QPushButton('Ответить')
button2 = QPushButton('Ok')


wintext = QLabel('Поздровляю! Ты ответил правильно на вопрос')
losetext = QLabel('Жаль, но ты ответил неправильно на вопрос')
wintext.hide()
button2.hide()
losetext.hide()
result.hide()
layout1.addWidget(result, alignment=Qt.AlignHCenter)
layout1.addWidget(qestbutton, alignment=Qt.AlignHCenter)
layout1.addWidget(wintext, alignment=Qt.AlignHCenter)
layout1.addWidget(losetext, alignment=Qt.AlignHCenter)
layout2.addWidget(radio1)
layout2.addWidget(radio2)
layout3.addWidget(radio3)
layout3.addWidget(radio4)
layout4.addWidget(button, alignment=Qt.AlignHCenter)
layout4.addWidget(button2, alignment=Qt.AlignHCenter)
layout5.addLayout(layout6)
layout5.addLayout(layout2)
layout5.addLayout(layout3)

group_box.setLayout(layout5)

main_layout.addLayout(layout1)
main_layout.addWidget(group_box)
main_layout.addLayout(layout4)

button.clicked.connect(check)
button2.clicked.connect(rec)

buttons()
#Запуск
main_win.setLayout(main_layout) 
main_win.show() 

app.exec_()





