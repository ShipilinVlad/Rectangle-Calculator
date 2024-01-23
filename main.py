import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGraphicsScene,
                             QGraphicsView, QGraphicsRectItem,
                             QVBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QColor, QBrush


class RectangleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        self.label1 = QLabel('Прямоугольник 1:')
        self.rect1_x1 = QLineEdit(self)
        self.rect1_y1 = QLineEdit(self)
        self.rect1_x2 = QLineEdit(self)
        self.rect1_y2 = QLineEdit(self)

        self.label2 = QLabel('Прямоугольник 2:')
        self.rect2_x1 = QLineEdit(self)
        self.rect2_y1 = QLineEdit(self)
        self.rect2_x2 = QLineEdit(self)
        self.rect2_y2 = QLineEdit(self)

        self.calculate_button = QPushButton('Рассчитать', self)
        self.calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel('Результат:')
        self.result_intersection = QLabel('Пересечение:')
        self.result_union = QLabel('Объединение:')
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 2000, 1500)
        self.setWindowTitle(
            'Площадь пересечения и объединения прямоугольников')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.rect1_x1)
        vbox.addWidget(self.rect1_y1)
        vbox.addWidget(self.rect1_x2)
        vbox.addWidget(self.rect1_y2)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.rect2_x1)
        vbox.addWidget(self.rect2_y1)
        vbox.addWidget(self.rect2_x2)
        vbox.addWidget(self.rect2_y2)
        vbox.addWidget(self.calculate_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.result_intersection)
        vbox.addWidget(self.result_union)
        vbox.addWidget(self.view)

        self.setLayout(vbox)

    def calculate(self):
        pass

    def intersection_rectangle(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x_intersection = max(x1, x3)
        y_intersection = max(y1, y3)
        width_intersection = min(x2, x4) - x_intersection
        height_intersection = min(y2, y4) - y_intersection

        return (x_intersection, y_intersection,
                width_intersection, height_intersection)

    def calculate_union(self, x1, y1, x2, y2, x3, y3, x4, y4):
        pass

    def calculate_area(self, rect):
        return rect[2] * rect[3]

    def draw_rectangles(self, x1, y1, x2, y2,
                        x3, y3, x4, y4, intersection_rect):
        self.scene.clear()

        rect1 = QGraphicsRectItem(x1, y1, x2 - x1, y2 - y1)
        rect2 = QGraphicsRectItem(x3, y3, x4 - x3, y4 - y3)

        brush = QBrush(QColor(0, 0, 255, 100))
        rect1.setBrush(brush)
        rect2.setBrush(brush)

        self.scene.addItem(rect1)
        self.scene.addItem(rect2)
        if not (x2 < x3 or y2 < y3):
            intersection_item = QGraphicsRectItem(intersection_rect[0],
                                                  intersection_rect[1],
                                                  intersection_rect[2],
                                                  intersection_rect[3])
            intersection_item.setBrush(QBrush(QColor(0, 0, 255, 100)))
            self.scene.addItem(intersection_item)

        self.view.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RectangleApp()
    ex.show()
    sys.exit(app.exec_())
