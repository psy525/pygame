from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class ScoreWindow(QMainWindow):
    def __init__(self, score):
        super().__init__()
        self.ui=uic.loadUi('../resources/score.ui', self)
        self.setStyleSheet("""
                        QMainWindow {
                            background-image: url(C:/workspace/개인공부/pygame/pythonProject/resources/images/score.png);
                        }
                    """)
        self.update_score(score)
        print(self.scoreLabel)
        self.show()

    def update_score(self, score):
        self.ui.scoreLabel.setText(f"점수 \n\n{score}점")