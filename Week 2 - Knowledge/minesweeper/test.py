from minesweeper import Sentence, MinesweeperAI

dummy = Sentence({1, 2, 3, 4},2)

dummer = MinesweeperAI()
print(dummer.mark_safe((2,3)))
print(dummer.make_safe_move())