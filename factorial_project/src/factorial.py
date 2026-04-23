class FactorialCalculator:
    """
    Calculates the factorial of a non-negative integer.
    """

    def calculate(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")

        if n < 0:
            raise ValueError("Negative input not allowed")

        result = 1
        for i in range(1, n + 1):
            result *= i

        return result