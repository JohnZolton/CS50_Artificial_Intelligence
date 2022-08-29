# CS50_Artificial_Intelligence
Harvard CS50's Introduction to Artificial Intelligence with Python

## Week 1 - Search
- [Degrees](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%201%20-%20Search/degrees): uses a breadth-first search to find minimum degrees of separation between two actors (source and target) via their co-stars. Initializes the first actor as a node with their id and adds their co-stars to the frontier. Then explores each movie's stars for the target star and repeats for each of their movies until it finds a connection. 

![image](https://user-images.githubusercontent.com/102374100/184661261-0cdd9870-0372-48cb-8e4b-855a5dad8ea9.png)

- [Tic Tac Toe](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%201%20-%20Search/tictactoe): uses an adversarial search to find the optimal move in a game of tictactoe. Assigns scores for each outcome (1 X wins, 0 tie, -1 O wins). Functions for the min player and max player call eachother to simulate an optimally played game for each possible move and the best possible move is chosen.

## Week 2 - Knowledge
- [Knights](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%202%20-%20Knowledge/knights): Uses knowledge bases to solve a series of logic puzzles. Knights always tell the truth and Knaves always lie. Converted game conditions to logic statements. All possible models were enumerated and the true one was selected to solve each problem.

- [Minesweeper](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%202%20-%20Knowledge/minesweeper): An AI to play minesweeper. Uses a knowledge base of logical sentences (sets of cells = # of nearby mines) to determine safe moves to make. A successful move reveals new sentences, those new sentences are deducted from existing sentences to draw new inferences and build a bank of safe cells. 

## Week 3 - Uncertainty
- [Pagerank](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%203%20-%20Uncertainty/pagerank): Calculates rankings for webpages based on probability distributions of a user navigating to each webpage (on their own or via a link from another webpage). Probability distributions were calculated using a transition model (returned a distribution of which page a user might visit next given a current page), a sampling model (starts at a random page and samples n pages using transition model to build a probability distribution for all pages), and an iterative page rank model (Initializes each page with base probability 1/(total pages) then repeatedly calculates new probabilities for each page based on the # of pages that link to it. Stops when the difference between the iterations are < .001).

- [Heredity] (https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%203%20-%20Uncertainty/heredity): Caculates the joint probability of a child inheriting a trait from their parents, given knowledge of the parents exhibiting a trait and probabilities of the # of genes the parents have and may give to the child.
