from functools import partial

class Bowling:
    def __init__(self):
        pass

    def frame_to_score(frame, first_bonus_points=0, second_bonus_points=0):
        if len(frame) == 1:
            # strike
            if frame == "X":
                score = 10
        if len(frame == 2):
            # both misses
            if frame[0] == "-" and frame[1] == "-":
                score = 0
            # first numeric pins, second miss
            if frame[0].isdigit() and frame[1] == "-":
                score = int(frame[0])
            # two numeric pins
            if frame[0].isdigit() and frame[1].isdigit():
                score = int(frame[0]) + int(frame[1])
            # first numeric pins, second spare
            if frame[0].isdigit() and frame[1] == "/":
                score = 10

        return score + first_bonus_points() + second_bonus_points()

    def frame_to_partially_apply_indexes(frame):
        if frame.contains("X"):
            return 2 # next 2 frames partially apply
        if frame.contains("/"):
            return 1 # next 1 frame partially apply

    def solve(self, input) -> int:
        tokens = input.split(' ')
        score_frame_partials = []
        partial_applications = {} # maps index to how many next frames to apply

        for idx, token in enumerate(tokens):
            score_frame_partials.append(partial(frame_to_score, token))

            partially_apply_frames = frame_to_partially_apply_indexes(token)
            if partially_apply_frames != None:
                partial_applications[idx] = partially_apply_frames

        return -1