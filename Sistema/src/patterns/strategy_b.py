from Sistema.src.patterns.strategy import Strategy
from typing import List

class StrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))
