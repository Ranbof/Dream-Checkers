from checkers.enums import CheckerType, SideType
from checkers.point import Point


# Размер поля
X_SIZE = Y_SIZE = 8

# Размер ячейки (в пикселях)
CELL_SIZE = 75

# Цвет фона меню
MENU_COLOR = "#BC987E"

# Скорость анимации (больше = быстрее)
ANIMATION_SPEED = 5

# Ширина рамки (Желательно должна быть чётной)
BORDER_WIDTH = 2 * 2

# Цвета игровой доски
FIELD_COLORS = ['#E7CFA9', '#927456']
# Цвет рамки при наведении на ячейку мышкой
HOVER_BORDER_COLOR = '#54b346'
# Цвет рамки при выделении ячейки
SELECT_BORDER_COLOR = '#944444'
# Цвет кружков возможных ходов
POSIBLE_MOVE_CIRCLE_COLOR = '#944444'

# Возможные смещения ходов шашек
MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

# Массивы типов белых и чёрных шашек
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN]