class Stats():  # statistics

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('hs.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        self.guns_left = 2
        self.score = 0

