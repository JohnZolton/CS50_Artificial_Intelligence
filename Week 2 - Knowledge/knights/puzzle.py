from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # base game condition, can't be both a knight and a knave
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), 
    # info from problem
    Biconditional(AKnight, And(AKnight, AKnave)),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # base game condition, can't be both a knight and a knave
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), 
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), 
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)), 
    # info from problem
    # A says we are both knaves
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnave))

    
    # P->Q is true if P and Q are true (Or if P and Q are false)
    # = not P or Q
    # so if someone is a knight (P) then what they say (Q) is true
    # if someone is a knave what they say will be false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # base game condition, can't be both a knight and a knave
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), 
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), 
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)), 
    # A is a knight and what they say is true
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # A is a knave and what they say is false
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # B is a knight and what they say is true
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # B is a knave and what they say is false
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # base game condition, can't be both a knight and a knave
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), 
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)), 
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)), 
    # A is a knight and what they said is true
    Biconditional(AKnight, Or(AKnight, AKnave)),
    
    # B says A said "i am a knave"
    Biconditional(BKnight, Implication(Or(AKnight, AKnave), AKnave)),
    
    # B says C is a knave
    Biconditional(BKnight, CKnave),
    
    # C says A is a knight
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
