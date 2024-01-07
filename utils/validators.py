class Validator:
    @staticmethod
    def empty(value):
        return not bool(value.strip())

    @staticmethod
    def positive(value):
        num_value = float(value)
        if num_value > 0:
            return True
        else:
            return False

