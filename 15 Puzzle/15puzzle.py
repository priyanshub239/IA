#!/usr/bin/env python3


from prettytable import PrettyTable
import math


puzzle_size = 16


#lista de matrizes
class state:
    def _init_(self, matrix, parent):
        self.matrix = matrix
        self.state = state
        self.parent = parent
        self.children = list()


def move(state, position):
    #position can be 1, 2, 3, 4 = up, down, left, right
    
    new_state = state
    
    if position == 1:
        print("Up")
    elif position == 2:
        print("Down")
    elif position == 3:
        print("Left")
    elif position == 4:
        print("Right")


def newMatrix(config):
    """

    :param config: array of the initial config
    :return: returns the generated matrix
    """
    matrix = [[0 for x in range(4)] for y in range(4)]

    it = 0
    for i in range(0,4):
        for j in range(0,4):
            matrix[i][j] = config[it]
            it += 1

    return matrix


def createMenu():
    table = PrettyTable(['Strategies', 'Options'])
    table.add_row(['DFS', 1])
    table.add_row(['BFS', 2])
    table.add_row(['IDFS', 3])
    table.add_row(['Greedy', 4])
    table.add_row(['A*', 5])
    print(table)


def hasSolution(config):
    """
    Function to check whether any game state is solvable.
    Formula:
       a. If the grid width is odd, then the number of inversions in a solvable
       situation is even.
       b. If the grid width is even, and the blank is on an even row counting
       from the bottom (second-last, fourth-last etc), then the number of
       inversions in a solvable situation is odd.
       c. If the grid width is even, and the blank is on an odd row counting
       from the bottom (last, third-last, fifth-last etc) then the number of
       inversions in a solvable situation is even.
    :param config: configuration array
    :return: returns true or false based on the formula specified above.
    """
    n_inv = 0
    blank_row = math.ceil((16 - config.index(0)) / 4)
    print("Blank Row: %d" % blank_row)
    for i in range(0, puzzle_size):
        for j in range(i+1, puzzle_size):
            if config[i] > config[j] and config[j] != 0:
                #print("%d %d" %(config[i], config[j]))
                n_inv += 1
    print("number of inversions: %d" % n_inv)
    return (blank_row % 2 != 0) == (n_inv % 2 == 0)
    

def DFS(initialConfig, finalConfig): #verificar se o no ja existe
    stack = initialConfig
    visited = set()
    while stack:
        node = stack.pop()
        visited.add(node)
        if node not in visited:
            stack.push()
        print(node)
        print(visited)
    print(stack)


initialConfig = list(map(int, input("Initial Configuration: ").split()))
finalConfig = list(map(int, input("Final Configuration: ").split()))
print("\n")
print(initialConfig)
print(finalConfig)
if not (hasSolution(initialConfig) == hasSolution(finalConfig)):
    print("This 15 puzzle has no solution.")
else:
    print("This 15 puzzle has solution.")
    #matrix = newMatrix(config)
    #print(matrix)
    createMenu()
    option = input('Option: ')
    if option == '1':
        print("DFS")
        DFS(initialConfig, finalConfig)
    elif option == '2':
        print("BFS*")
    elif option == '3':
        print("IDFS")
    elif option == '4':
        print("Greedy")
    elif option == '5':
        print("A*")


