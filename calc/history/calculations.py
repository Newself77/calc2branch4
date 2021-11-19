"""Calculation history class"""


class Calculations:
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clearing the history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        return Calculations.history[-1]

    def get_calculation(self):
        """ get a specific calculation from history"""
        return Calculations.history[self]

    @staticmethod
    def add_calculations(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
