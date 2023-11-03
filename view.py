import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from Controller import CalculatorController
from model import CalculatorModel

class CalculatorView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Calculator with Data Size Converter")
        self.setGeometry(100, 100, 300, 400)
        
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.result_display = QLineEdit(self)
        self.layout.addWidget(self.result_display)
        
        buttons = [
            "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", "C", "=", "+",
            "Bits to Bytes", "Bytes to Bits", "Bytes to Kilobytes", "Kilobytes to Bytes", "Kilobytes to Megabytes", "Megabytes to Kilobytes"
        ]
        
        button_grid = QVBoxLayout()
        for label in buttons:
            button = QPushButton(label, self)
            button.clicked.connect(self.on_button_click)
            button_grid.addWidget(button)
        
        self.layout.addLayout(button_grid)
        self.setLayout(self.layout)
        
    def on_button_click(self):
        sender = self.sender()
        current_text = self.result_display.text()
        button_text = sender.text()
        
        if button_text == "=":
            result = self.controller.handle_expression(current_text)
            self.result_display.setText(result)
        elif button_text == "C":
            self.result_display.clear()
        elif button_text in ["Bits to Bytes", "Bytes to Bits", "Bytes to Kilobytes", "Kilobytes to Bytes", "Kilobytes to Megabytes", "Megabytes to Kilobytes"]:
            result = self.controller.handle_data_size_conversion(current_text, button_text)
            self.result_display.setText(result)
        else:
            self.result_display.setText(current_text + button_text)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = CalculatorModel()
    controller = CalculatorController(model)
    calc_app = CalculatorView(controller)
    calc_app.show()
    sys.exit(app.exec_())
