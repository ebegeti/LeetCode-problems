class SnakeGame:

    def __init__(self, width,height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.x_pos = 0
        self.y_pos = 0
        self.score = 0
        self.path = [[0, 0]]

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.path[0]
        if direction == "R":
            self.y_pos += 1
        elif direction == "L":
            self.y_pos -= 1
        elif direction == "U":
            self.x_pos -= 1
        elif direction == "D":
            self.x_pos += 1
        if (self.x_pos < self.height and self.y_pos < self.width) and (self.x_pos >= 0 and self.y_pos >= 0) and [self.x_pos, self.y_pos] not in self.path[ :-1]:
            if len(self.food) > 0:
                if [self.x_pos, self.y_pos] == self.food[0]:
                    self.path.insert(0, [self.x_pos, self.y_pos])
                    self.score += 1
                    self.food.remove(self.food[0])
                    print(self.score)
                    return self.score
            print(self.score)
            return self.score
        else:
            print(-1)
            return -1

# Your SnakeGame object will be instantiated and called as such:
obj = SnakeGame(3, 2, [[1,2],[0,1]])
param_1 = obj.move('R')
param_1 = obj.move('D')
param_1 = obj.move('R')
param_1 = obj.move('U')
param_1 = obj.move('L')
param_1 = obj.move('U')
