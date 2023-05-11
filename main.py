import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget


if __name__ == '__main__':
    app = QApplication([])

    # Create your application's GUI
    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(500, 100, 280, 80)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)

    # Show application's GUI
    window.show()

    # Run application's event loop
    sys.exit(app.exec())
