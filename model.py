ERROR_MSG = 'ERROR!!!!!. UNidentified Operator'

class CalculatorModel:
    def evaluate_expression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
        return result

    def convert_data_size(self, value, conversion_type):
        try:
            value = float(value)
            if conversion_type == "Bits to Bytes":
                result = value / 8
            elif conversion_type == "Bytes to Bits":
                result = value * 8
            elif conversion_type == "Bytes to Kilobytes":
                result = value / 1000
            elif conversion_type == "Kilobytes to Bytes":
                result = value * 1000
            elif conversion_type == "Kilobytes to Megabytes":
                result = value / 1000
            elif conversion_type == "Megabytes to Kilobytes":
                result = value * 1000
            else:
                result = ERROR_MSG
            return str(result)
        except ValueError:
            return ERROR_MSG
