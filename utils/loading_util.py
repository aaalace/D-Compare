from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
        self.movie = QMovie('static/loading.gif')
        self.label_animation = QLabel(self)
        self.label_animation.setMovie(self.movie)
        self.movie.start()
