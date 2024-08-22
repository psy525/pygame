from PyQt5.QtWidgets import QApplication
import sys
from crud.score.score import ScoreWindow  # ScoreWindow 클래스를 가져옵니다.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    score = 2000  # 예시 점수
    window = ScoreWindow(score)
    window.show()
    sys.exit(app.exec_())