from model import CalculatorModel

class CalculatorController:
    def __init__(self, model):
        self.model = model

    def handle_expression(self, expression):
        return self.model.evaluate_expression(expression)

    def handle_data_size_conversion(self, value, conversion_type):
        return self.model.convert_data_size(value, conversion_type)
