import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGraphicsScene,
                             QGraphicsView, QGraphicsRectItem,
                             QVBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QColor, QBrush


class RectangleApp(QWidget):
    """
        Главный класс приложения для работы с прямоугольниками.

        Этот класс нужен для создания окна приложения, всех полей для
        ввода информации о прямоугольниках, рисования самих
        прямоугольников на сцене, а также вычисления площадей их
        пересечения и объединения

        Attributes:
            - scene (QGraphicsScene): Объект сцены для отображения графики.
            - view (QGraphicsView): Виджет для отображения объектов
        QGraphicsScene.
            - label1, label2 (QLabel): Метки для описания полей ввода
        прямоугольников.
            - rect1_x1, rect1_y1, rect1_x2, rect1_y2 (QLineEdit): Поля
        ввода координат первого прямоугольника.
            - rect2_x1, rect2_y1, rect2_x2, rect2_y2 (QLineEdit): Поля
        ввода координат второго прямоугольника.
            - calculate_button (QPushButton): Кнопка для рассчета и о
        тображения результатов.
            - result_label (QLabel): Метка для вывода результатов.
            - result_intersection, result_union (QLabel): Метки для вывода
        площади пересечения и объединения.

        Methods:
            - initUI(): Инициализация интерфейса пользователя.
            - calculate(): Рассчет и отображение результатов при нажатии на
        кнопку.
            - intersection_rectangle(x1, y1, x2, y2, x3, y3, x4, y4): Рассчет
        координат пересечения двух прямоугольников.
            - calculate_union(x1, y1, x2, y2, x3, y3, x4, y4): Рассчет площади
        объединения двух прямоугольников.
            - calculate_area(rect): Рассчет площади прямоугольника.
            - draw_rectangles(x1, y1, x2, y2, x3, y3, x4, y4,
        intersection_rect): Отображение прямоугольников на сцене.
        """
    def __init__(self):
        """Инициализация класса RectangleApp."""
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
        """
                Инициализация интерфейса пользователя.

                Устанавливает геометрию и заголовок окна, создает и настраивает
                компоненты интерфейса, такие как строки с названиями
                параметров, строки для ввода этих параметров и кнопка,
                по которой и запускается выполнение расчётов и рисование
                прямоугльников
                """
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
        """
                Рассчет и отображение результатов при нажатии на кнопку.

                Обрабатывает данные в QLineEdit-ах, которые ввёл пользователь,
                рассчитывает площадь пересечения и объединения, отображает
                прямоугольники и результаты на сцене, либо выдаёт ошибку вместо
                площадей пересечения и объединения

                Attributes:
                    -

                Returns:
                    -

                Raises:
                    ValueError.

                Examples:
                    calculate(self):
                        1) Если параметры rect1_x1, rect1_y1, rect1_x2,
                        rect1_y2 и rect2_x1, rect2_y1, rect2_x2, rect2_y2 -
                        целые числа, то по нажатию кнопки программа выполнит
                        свою задачу.
                        2) Если же хоть один из этих параметров не целое число,
                        то в полях Пересечение и Объединение будет написано
                        'Ошибка ввода!'
                """
        try:
            rect1_x1 = int(self.rect1_x1.text())
            rect1_y1 = int(self.rect1_y1.text())
            rect1_x2 = int(self.rect1_x2.text())
            rect1_y2 = int(self.rect1_y2.text())

            rect2_x1 = int(self.rect2_x1.text())
            rect2_y1 = int(self.rect2_y1.text())
            rect2_x2 = int(self.rect2_x2.text())
            rect2_y2 = int(self.rect2_y2.text())

            intersection_rect = self.intersection_rectangle(rect1_x1, rect1_y1,
                                                            rect1_x2, rect1_y2,
                                                            rect2_x1, rect2_y1,
                                                            rect2_x2, rect2_y2)

            self.draw_rectangles(rect1_x1, rect1_y1,
                                 rect1_x2, rect1_y2,
                                 rect2_x1, rect2_y1,
                                 rect2_x2, rect2_y2, intersection_rect)

            intersection_area = self.calculate_area(intersection_rect)
            union_area = self.calculate_union(rect1_x1, rect1_y1,
                                              rect1_x2, rect1_y2,
                                              rect2_x1, rect2_y1,
                                              rect2_x2, rect2_y2)

            self.result_intersection.setText(
                f'Пересечение: {intersection_area}')
            self.result_union.setText(f'Объединение: {union_area}')
        except ValueError:
            self.result_intersection.setText(
                f'Пересечение: Ошибка ввода данных!')
            self.result_union.setText(f'Объединение: Ошибка ввода данных!')

    def intersection_rectangle(self, x1, y1, x2, y2, x3, y3, x4, y4) -> tuple:
        """
                Вычисление прямоугольника пересечения между двумя
                прямоугольниками.

                Attributes:
                    -x1 (int): x-координата верхнего левого угла первого
                    прямоугольника.
                    -y1 (int): y-координата верхнего левого угла первого
                    прямоугольника.
                    -x2 (int): x-координата нижнего правого угла первого
                    прямоугольника.
                    -y2 (int): y-координата нижнего правого угла первого
                    прямоугольника.
                    -x3 (int): x-координата верхнего левого угла второго
                    прямоугольника.
                    -y3 (int): y-координата верхнего левого угла второго
                    прямоугольника.
                    -x4 (int): x-координата нижнего правого угла второго
                    прямоугольника.
                    -y4 (int): y-координата нижнего правого угла второго
                    прямоугольника.

                Returns:
                    tuple: (x, y, ширина, высота) представляющий
                    прямоугольник пересечения.

                """
        x_intersection = max(x1, x3)
        y_intersection = max(y1, y3)
        width_intersection = min(x2, x4) - x_intersection
        height_intersection = min(y2, y4) - y_intersection

        return (x_intersection, y_intersection,
                width_intersection, height_intersection)

    def calculate_union(self, x1, y1, x2, y2, x3, y3, x4, y4) -> int:
        """
                Вычисление площади объединения двух прямоугольников.

                Аргументы:
                    -x1 (int): x-координата верхнего левого угла первого
                    прямоугольника.
                    -y1 (int): y-координата верхнего левого угла первого
                    прямоугольника.
                    -x2 (int): x-координата нижнего правого угла первого
                    прямоугольника.
                    -y2 (int): y-координата нижнего правого угла первого
                    прямоугольника.
                    -x3 (int): x-координата верхнего левого угла второго
                    прямоугольника.
                    -y3 (int): y-координата верхнего левого угла второго
                    прямоугольника.
                    -x4 (int): x-координата нижнего правого угла второго
                    прямоугольника.
                    -y4 (int): y-координата нижнего правого угла второго
                    прямоугольника.

                Возвращаемое значение:
                    int: Площадь объединения прямоугольников.

                """
        intersection_area = self.calculate_area(self.intersection_rectangle(
            x1, y1, x2, y2, x3, y3, x4, y4))
        if intersection_area == 0:
            return int(abs((x2 - x1) * (y2 - y1)) + abs((x4 - x3) * (y4 - y3)))
        return int(abs((x2 - x1) * (y2 - y1)) +
                   abs((x4 - x3) * (y4 - y3)) - intersection_area)

    def calculate_area(self, rect) -> int:
        """
                Вычисление площади прямоугольника.

                Аргументы:
                    rect (tuple): Кортеж (x, y, ширина, высота)
                    представляющий прямоугольник.

                Возвращаемое значение:
                    int: Площадь прямоугольника.

                """
        rect = list(rect)
        if rect[2] < 0 or rect[3] < 0:
            return 0
        return rect[2] * rect[3]

    def draw_rectangles(self, x1, y1, x2, y2,
                        x3, y3, x4, y4, intersection_rect):
        """
                Отрисовка прямоугольников и их пересечения на QGraphicsScene.

                Функция очищает текущую сцену, затем рисует 2 прямоугольника,
                после чего дорисовывает более насыщенным цветом прямоугольник,
                 в котором пересекаются два первоночальных, если они
                 пересекаются

                Аргументы:
                    x1 (int): x-координата верхнего левого угла первого
                    прямоугольника.
                    y1 (int): y-координата верхнего левого угла первого
                    прямоугольника.
                    x2 (int): x-координата нижнего правого угла первого
                    прямоугольника.
                    y2 (int): y-координата нижнего правого угла первого

                    прямоугольника.
                    x3 (int): x-координата верхнего левого угла второго
                    прямоугольника.
                    y3 (int): y-координата верхнего левого угла второго
                    прямоугольника.
                    x4 (int): x-координата нижнего правого угла второго
                    прямоугольника.
                    y4 (int): y-координата нижнего правого угла второго
                    прямоугольника.
                    intersection_rect (tuple): Кортеж (x, y, ширина, высота)
                    представляющий прямоугольник пересечения.

                """
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
