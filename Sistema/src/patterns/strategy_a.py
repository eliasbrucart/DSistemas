from Sistema.src.patterns.strategy import Strategy
from typing import List

class StrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)