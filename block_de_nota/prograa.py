import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QMessageBox, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QFileDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Menubar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Actions
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.setWindowTitle('Notepad')
        self.setGeometry(100, 100, 600, 400)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')
        if filename:
            text = self.text_edit.toPlainText()
            with open(filename, 'w') as f:
                f.write(text)
            QMessageBox.information(self, 'Info', 'File saved successfully.')

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')
        if filename:
            with open(filename, 'r') as f:
                text = f.read()
            self.text_edit.setPlainText(text)
            QMessageBox.information(self, 'Info', 'File opened successfully.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    window.show()
    sys.exit(app.exec_())
