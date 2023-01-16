# coding: utf-8
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Canvas(QWidget):      #Основной класс со всеми функциями
    def __init__(self):
        super(Canvas, self).__init__()

        self.objects = []
        self.instrument = 'brush'
        self.green = 0
        self.red = 0
        self.blue = 0
        self.size = 10
        self.x = 0
        self.y = 0
        

        h = 1080
        w = 1920
        self.saveName = "None"
        self.start = QPoint()
        self.myPenColor = (Qt.black)
        self.image = QImage(w, h, QImage.Format_RGB32)
        self.image2 = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.screen_color = (Qt.white)
        self.image.fill(self.screen_color)
        self.image2.fill(Qt.white)
        self.update()

    def paintEvent(self, event):        #Отрисовка объектов
        if self.instrument == 'brush':
            painter = QPainter(self)
            painter.drawImage(event.rect(), self.image, self.rect())
            painter.end()
        if self.instrument == 'line':
            painter = QPainter(self)
            painter.drawImage(self.rect(), self.image, self.rect())
            painter.end()
        if self.instrument == 'circle':
            painter = QPainter(self)
            painter.drawImage(self.rect(), self.image, self.rect())
            painter.end()
        if self.instrument == 'eraser':
            painter = QPainter(self)
            painter.drawImage(event.rect(), self.image, self.rect())
            painter.end()

    def mousePressEvent(self, event):       #Считывание нажатия мышки
        self.path.moveTo(event.pos())
        self.start = event.pos()
        self.x = event.x()
        self.y = event.y()

    def mouseMoveEvent(self, event):        #Считывание движения мышки
        if self.instrument == 'brush':
            self.path.lineTo(event.pos())
            p = QPainter(self.image)
            p.setPen(QPen(self.myPenColor, self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawPath(self.path)
            p.end()
            self.update()
        elif self.instrument == 'line':
            self.image = self.image2.copy()
            painter = QPainter(self.image)
            painter.setPen(QPen(self.myPenColor, self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.start, event.pos())
            self.update()
        elif self.instrument == 'eraser':
            self.path.lineTo(event.pos())
            p = QPainter(self.image)
            p.setPen(QPen(self.screen_color, self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            p.drawPath(self.path)
            p.end()
            self.update()
        elif self.instrument == 'circle':
            self.image = self.image2.copy()
            self.path.lineTo(event.pos())
            p = QPainter(self.image)
            p.setPen(QPen(self.myPenColor, self.size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            s = ((event.x() - self.x) ** 2 + (event.y() - self.y) ** 2) ** 0.5
            p.drawEllipse(self.start, s, s)
            self.path.clear()
            p.end()
            self.update()

    def mouseReleaseEvent(self, event):     #Отжатие конпки мыши
        if self.instrument == 'brush':
            self.image2 = self.image.copy()
        if self.instrument == 'line':
            self.image2 = self.image.copy()
        if self.instrument == 'circle':
            self.image2 = self.image.copy()
        if self.instrument == 'eraser':
            self.image2 = self.image.copy()

    def setBrush(self):          #Инструмент кисть
        self.instrument = 'brush'

    def setLine(self):           #Инструмент линия
        self.instrument = 'line'

    def setCircle(self):         #Инстркмент круг
        self.instrument = 'circle'

    def setSquare(self):         #Инструмент квадрат
        pass

    def setEraser(self):         #Инструмент ластик
        self.instrument = 'eraser'
        self.path.clear()

    def setGrain(self):          #Инструмен  заливка
        pass

    def color_(self):     #Цветовая палитра
        col = QColorDialog.getColor()
        self.myPenColor = col
        self.path.clear()

    def red_value(self):        #Красный цвет
        self.red = 255
        self.green = 0
        self.blue = 0
        self.myPenColor = (Qt.red)
        self.path.clear()

    def orange_value(self):     #Оранжевый цвет
        self.red = 255
        self.green = 155
        self.blue = 0
        self.myPenColor = QColor(255, 155, 0)
        self.path.clear()

    def yellow_value(self):     #Желтый цвет
        self.red = 255
        self.green = 255
        self.blue = 0
        self.myPenColor = (Qt.yellow)
        self.path.clear()

    def green_value(self):     #Зеленый цвет
        self.red = 0
        self.green = 255
        self.blue = 0
        self.myPenColor = (Qt.green)
        self.path.clear()

    def light_blue_value(self):     #Голубой цвет
        self.red = 30
        self.green = 144
        self.blue = 255
        self.myPenColor = (Qt.cyan)
        self.path.clear()

    def blue_value(self):       #Синий цвет
        self.red = 0
        self.green = 0
        self.blue = 255
        self.myPenColor = (Qt.blue)
        self.path.clear()

    def violet_value(self):     #Фиолетовый цвет
        self.red = 138
        self.green = 43
        self.blue = 226
        self.myPenColor = (Qt.magenta)
        self.path.clear()

    def black_value(self):      #Черный цвет
        self.red = 0
        self.green = 0
        self.blue = 0
        self.myPenColor = (Qt.black)
        self.path.clear()

    def white_value(self):      #Белый цвет
        self.red = 255
        self.green = 255
        self.blue = 255
        self.myPenColor = (Qt.white)
        self.path.clear()

    def small_value(self):      #Маленькая толщина
        self.size = 1
        self.path.clear()

    def med_value(self):        #Средняя толщинв
        self.size = 10
        self.path.clear()

    def big_value(self):        #Большая толщина
        self.size = 60
        self.path.clear()

    def setOpen(self):      #Открытие файла
        openName = QFileDialog.getOpenFileNames()
        self.image.load(*openName[0])
        openName = str(*openName[0])
        self.saveName = openName
        print(self.saveName)

    def setImColor(self):       #Настройка цвета фона
        col = QColorDialog.getColor()
        self.screen_color = col
        self.image.fill(col)
        
    def saveImage(self):        #Функция сохранения
        if self.saveName == "None":
            self.saveAsImage()
        else:
            self.image.save(self.saveName)
            
        
    def saveAsImage(self):      #Функция "сохранить как"
        self.saveName = QFileDialog.getSaveFileName()
        self.saveName = self.saveName[0].split('/')[-1]
        self.image.save(self.saveName+".png")         


class Window(QMainWindow):  #Класс для взаимодействия с интерфейсом
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("C:/Users/nikit/Desktop/проект/window.ui", self)

        self.setCentralWidget(Canvas())

        self.setWindowTitle('Графический редактор')

        self.color.triggered.connect(self.centralWidget().color_)

        self.op.triggered.connect(self.centralWidget().setOpen)
        self.sav.triggered.connect(self.centralWidget().saveImage)
        self.saas.triggered.connect(self.centralWidget().saveAsImage)

        self.action_brush_2.triggered.connect(self.centralWidget().setBrush)
        self.grain.triggered.connect(self.centralWidget().setGrain)  ####
        self.pip_2.triggered.connect(self.centralWidget().setEraser)

        self.action_line_2.triggered.connect(self.centralWidget().setLine)
        self.circle.triggered.connect(self.centralWidget().setCircle)
        self.action_square.triggered.connect(self.centralWidget().setSquare)  ####

        self.canv_col.triggered.connect(self.centralWidget().setImColor)

        self.red.triggered.connect(self.centralWidget().red_value)
        self.orange.triggered.connect(self.centralWidget().orange_value)
        self.yellow.triggered.connect(self.centralWidget().yellow_value)
        self.green.triggered.connect(self.centralWidget().green_value)
        self.light_blue.triggered.connect(self.centralWidget().light_blue_value)
        self.blue.triggered.connect(self.centralWidget().blue_value)
        self.violet.triggered.connect(self.centralWidget().violet_value)
        self.black.triggered.connect(self.centralWidget().black_value)
        self.white.triggered.connect(self.centralWidget().white_value)

        self.small.triggered.connect(self.centralWidget().small_value)
        self.med.triggered.connect(self.centralWidget().med_value)
        self.big.triggered.connect(self.centralWidget().big_value)


if __name__ == '__main__':      #Основной цикл
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
