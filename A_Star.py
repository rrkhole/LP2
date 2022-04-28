class Block:
    def __init__(self, d, level, f_value):
        # Initialize the Block with the data, level of the node and the calculated f_value
        self.d = d
        self.level = level
        self.f_value = f_value

    def find_space(self, puzzle, a):
        # This function specifically used to find the position of the blank space
        for i in range(0, len(self.d)):
            for j in range(0, len(self.d)):
                if puzzle[i][j] == a:
                    return i, j

    def create_copy(self, block):
        # function to create a copy of similar matrix given in block
        temp = []
        for i in block:
            row = []
            for j in i:
                row.append(j)
            temp.append(row)
        return temp

    def move(self, puzzle, x1, y1, x2, y2):
        # function to move the blank space in the given direction and if the position value are out of limits the return None
        if x2 >= 0 and x2 < len(self.d) and y2 >= 0 and y2 < len(self.d):
            temp_puzzle = []
            temp_puzzle = self.create_copy(puzzle)
            temp = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp
            return temp_puzzle
        else:
            return None

    def generate_childBlocks(self):
        # function to generate child blocks from the given block by moving the blank space
        # either in the four directions {up,down,left,right}
        x, y = self.find_space(self.d, '_')
        # direction_list contains position values for moving the blank space in either of
        # the 4 directions [up,down,left,right] respectively.
        direction_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children_blocks = []
        for i in direction_list:
            child_block = self.move(self.d, x, y, i[0], i[1])
            if child_block is not None:
                child_block = Block(child_block, self.level + 1, 0)
                children_blocks.append(child_block)
        return children_blocks


class Puzzle:
    def __init__(self, size):
        # Initialize the puzzle size by the specified size,open and close lists to empty
        self.size = size
        self.open = []
        self.close = []

    def take_input(self):
        # function to take the puzzle input from the user
        puzzle = []
        for i in range(0, self.size):
            t = input().split(" ")
            puzzle.append(t)
        return puzzle

    def calculate_h(self, start, goal):
        # function to calculate h value(no. of misplaced blocks)
        h = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    h += 1
        return h

    def calculate_f(self, start, goal):
        # Function to calculate hueristic value f(x) = h(x) + g(x)
        return self.calculate_h(start.d, goal) + start.level

    def process(self):
        # Accept Start and Goal Puzzle state
        print("\nEnter the start state of puzzle \n")
        start = self.take_input()
        print("\nEnter the goal state of puzzle \n")
        goal = self.take_input()

        start = Block(start, 0, 0)
        start.f_value = self.calculate_f(start, goal)
        # Put the start block in the open list

        self.open.append(start)
        print("\n\n")
        while True:
            current = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in current.d:
                for j in i:
                    print(j, end=" ")
                print("")
            # If the difference between current and goal block is 0 we have reached the goal block
            if (self.calculate_h(current.d, goal) == 0):
                break
            for i in current.generate_childBlocks():
                i.f_value = self.calculate_f(i, goal)
                self.open.append(i)
            self.close.append(current)
            del self.open[0]

            # sort the open list based on f value
            self.open.sort(key=lambda x: x.f_value, reverse=False)


puzzle = Puzzle(3)
puzzle.process()
