from minesweeper import Sentence, MinesweeperAI

dummy = Sentence({1, 2, 3, 4},2)

dummer = MinesweeperAI()
print(dummer.knowledge)
dummer.add_knowledge((3,4), 2)
print(dummer.knowledge)