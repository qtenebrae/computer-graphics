import pytest

from src.app import App


class MockEvent:
    def __init__(self, keysym):
        self.keysym = keysym


@pytest.fixture(scope="module")
def app():
    app = App()
    yield app


def test_app_creation(app):
    """Тестирование создания объекта класса App."""
    assert app is not None
    assert app.title() == "Oval"
    assert app.resizable() == (False, False)


def test_set_coords(app):
    """Тестирование установки координат овала."""
    app.var_axleA.set(300)
    app.var_axleB.set(200)
    app.var_coordX.set(450)
    app.var_coordY.set(450)
    app.set_coords()
    assert app.firstCoord.x == 300
    assert app.firstCoord.y == 350
    assert app.secondCoord.x == 600
    assert app.secondCoord.y == 550


def test_paint(app):
    """Тестирование рисования овала на холсте."""
    app.var_axleA.set(300)
    app.var_axleB.set(200)
    app.var_coordX.set(450)
    app.var_coordY.set(450)
    app.currentColors = 1
    app.paint(None)
    assert app.figure is not None
    assert app.canvas.itemcget(app.figure, "fill") == "yellow"


def test_on_key_press(app):
    """Тестирование перемещения овала на холсте."""
    app.var_axleA.set(300)
    app.var_axleB.set(200)
    app.var_coordX.set(450)
    app.var_coordY.set(450)
    app.currentColors = 2
    app.paint(None)
    app.var_step.set(20)
    app.on_key_press(MockEvent("Left"))
    assert app.firstCoord.x == 280
    assert app.secondCoord.x == 580
    app.on_key_press(MockEvent("Right"))
    assert app.firstCoord.x == 300
    assert app.secondCoord.x == 600
    app.on_key_press(MockEvent("Up"))
    assert app.firstCoord.y == 330
    assert app.secondCoord.y == 530
    app.on_key_press(MockEvent("Down"))
    assert app.firstCoord.y == 350
    assert app.secondCoord.y == 550


def test_on_key_press_color(app):
    """Тестирование изменения цвета заливки овала."""
    app.var_axleA.set(300)
    app.var_axleB.set(200)
    app.var_coordX.set(450)
    app.var_coordY.set(450)
    app.currentColors = 3
    app.paint(None)
    app.on_key_press(MockEvent("bracketleft"))
    assert app.currentColors == 2
    assert app.canvas.itemcget(app.figure, "fill") == "red"
    app.on_key_press(MockEvent("bracketright"))
    assert app.currentColors == 3
    assert app.canvas.itemcget(app.figure, "fill") == "green"
