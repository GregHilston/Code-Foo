import sys
import json
import itertools
import heapq 

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

class AssignCookiesSolver():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def parse_input(self):
        with open(self.input_file_path) as f:
            data = json.load(f)

            return data["children"], data["cookies"]

    def solve(self):
        answer = 0

        children, cookies = self.parse_input()
        
        while len(children) != 0 or len(cookies) != 0:
            h = []

            for cookie in cookies:
                for child in children:
                    diff = cookie - child
                    # don't push illegal moves
                    if diff >= 0: 
                        heapq.heappush(h, (cookie - child, (child, cookie)))

                heapq.heapify(h)

            try:
                val = heapq.heappop(h)
            except:
                # because i'm lazy
                return answer
            
            best_diff = val[0]
            best_child = val[1][0]
            best_cookie = val[1][1]

            children.remove(best_child)
            cookies.remove(best_cookie)
            answer += 1

        return answer

assignCookiesSolver = AssignCookiesSolver("../../input_1.json")
print(assignCookiesSolver.solve())