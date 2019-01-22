import sys
import json

class BuySellStockSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        with open(self.input_file_path) as f:
            data = json.load(f)

            return data["input"]

    def solve(self):
        max_profit = 0
        input = self.parse_input()

        for index, stock_buy_price in enumerate(input):
            for stock_sell_price in input[index:]:
                if stock_sell_price - stock_buy_price > max_profit:
                    max_profit = stock_sell_price - stock_buy_price

        return max_profit