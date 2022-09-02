from collections import deque
import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains.copy(): #loop through all variables in domain
            for word in self.domains[var].copy(): # loop through values in variable
                if len(word) != var.length:
                    self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        removed = False
        overlap = self.crossword.overlaps[x, y]
        if overlap:
            for word1 in self.domains[x].copy():
                remove = True
                for word2 in self.domains[y]:
                    if (
                        word1[overlap[0]] == word2[overlap[1]]
                    ):
                        remove = False
                if remove:
                    self.domains[x].remove(word1)
                    removed = True
        return removed

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs == None:
            arcs = []
            # if no specified arcs, check every arc in the problem
            for j in self.domains:
                for k in self.crossword.neighbors(j):
                    if j == k: continue
                    arcs.append((j,k))
        # each arc is a tuple (x,y)
        # revise each arc one at a time
        while len(arcs) > 0:
            x, y = arcs.pop()
            if self.revise(x, y):
                if len(self.domains[x])==0:
                    return False
                #add arcs for all of x's neighbors
                for z in self.crossword.neighbors(x):
                    if z == y: continue # skip y
                    arcs.append((z,x))
        return True
            
            

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        return not bool(self.crossword.variables - set(assignment))
        """for key in assignment:
            if assignment[key] == None:
                return False
        return True
        """

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        used_words = set()
        for var in assignment:
            if assignment[var] not in used_words:
                used_words.add(assignment[var])
            else:
                return False
            
            if len(assignment[var]) != var.length:
                return False
            
            for neighbor in self.crossword.neighbors(var):
                if neighbor in assignment:
                    i,j = self.crossword.overlaps[var, neighbor]
                    if assignment[var][i] != assignment[neighbor][j]:
                        return False
        return True
        """
            for word in assignment[var]:
                # enforcing word length
                if var.length != len(word):
                    return False
                # no repeat words
                if assignment[var].count(word) > 1:
                    return False
                # no conflicts with neighboring values
                for vars in self.crossword.neighbors(var):
                    if vars in assignment:
                        overlap = self.crossword.overlaps[var, vars]
                        if assignment[var][overlap[0]] != assignment[vars][overlap[1]]:
                            return False
        return True"""

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        """counts = []
        for a in self.domains:
            if a == var: continue
            neighbors = self.crossword.neighbors(a)
            for x in assignment:
                neighbors.remove(x)
            counts.append((a, len(neighbors)))
        counts.sort(key = lambda x:x[1])
        return counts[0][0]"""
        counts = {}
        for word in self.domains[var]:
            counts[word] = 0
            for neighbor in self.crossword.neighbors(var) - assignment:
                if word in self.domains[neighbor]:
                    counts[word] +=1
        return counts.sort(key= counts.get)



    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        """
        tuples = []
        for var in self.crossword.variables - set(assignment):
            tuples.append(var, len(assignment[var]))
        tuples.sort(key = lambda x:x[1])
        # if theres a tie choose the one with the most neighbors
        if tuples.count(tuples[0][0]) > 1:
            # if there's a tie
            current = tuples[0] # first item in sorted list
            for x in tuples:
                if self.crossword.neighbors(x[0]) > self.crossword.neighbors(current[0]):
                    current = x 
            return current[0]
        return tuples[0][0]"""
        chosen = None
        for var in self.crossword.variables -set(assignment):
            if (
                chosen is None or
                len(self.domains[var]) < len(self.domains[chosen]) or
                len(self.crossword.neighbors(var)) > len(self.crossword.neighbors(chosen))
            ):
                chosen = var
        return chosen


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment): 
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.domains[var]:
            assignment[var] = value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result != None:
                    return result
                assignment.remove(var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
