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

- [Heredity](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%203%20-%20Uncertainty/heredity): Caculates the joint probability of a child inheriting a trait from their parents, given knowledge of the parents exhibiting a trait and probabilities of the # of genes the parents have and may give to the child.

## Week 4 - Optimization
- [Crossword](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%204%20-%20Optimization): (Constraint satisfaction problem) Generates a crossword given a board layout and list of potential words. Each variable (empty word on the board) has unary constraints (word length) and binary constraints (overlapping letter constraint with its neighbors). Finds a word for each variable that satisfies all the unary and binary constraints (if possible). Enforces node constency (removes words that don't match variable length), enforces arc consistency (removes possible words that would conflict with their neighbors), and uses Backtracking Search to assign words to locations based on a partial assignment. Backtracking search recursively tries to assign words to variables that satisfies the constraints. If constraints are violated, it tries a different assignment.

![image](https://user-images.githubusercontent.com/102374100/188275593-96fed8c4-2f8b-4ebe-ba80-cd86303cdb83.png)

## Week 5 - Learning
- [Shopping](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%205%20-%20Learning/shopping): An AI to predict whether online shopping customers will complete a purchase. Given information about a user ??? how many pages they???ve visited, whether they???re shopping on a weekend, what web browser they???re using, etc. ??? predicts whether or not the user will make a purchase using a K-Nearest-Neighbor classifier. The main function loads data from a CSV spreadsheet by calling the load_data function and splits the data into a training and testing set. The train_model function is then called to train a machine learning model on the training data. Then, the model is used to make predictions on the testing data set. Finally, the evaluate function determines the sensitivity and specificity of the model, before the results are ultimately printed to the terminal.

![image](https://user-images.githubusercontent.com/102374100/188322020-0aa850b0-1cb6-46d3-9eda-40d91723c25e.png)


- [Nim](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%205%20-%20Learning/nim): The game begins with some number of piles, each with some number of objects. Players take turns: on a player???s turn, the player removes any non-negative number of objects from any one non-empty pile. Whoever removes the last object loses.
Using Q-Learning, we try to learn a reward value (a number) for every (state, action) pair. An action that loses the game will have a reward of -1, an action that results in the other player losing the game will have a reward of 1, and an action that results in the game continuing has an immediate reward of 0, but will also have some future reward. Using the formula (New Q(state, action)) = Q(state, action) + (learning rate) * (new value estimate - old value estimate), existing Q-values are updated for each state/action pair. The learning rate is a factor that determines how much to value new information vs old information in the new Q value. The AI usually chooses the best move but will sometimes choose a random move to continue exploring new states. Then the AI trains on 10,000 games and becomes unbeatable (at least for me).

![image](https://user-images.githubusercontent.com/102374100/188501768-614ad15d-b28e-41eb-ac4a-394aba65ef17.png)

![image](https://user-images.githubusercontent.com/102374100/188501805-80066818-cab4-4a31-9f45-e4a8562edd69.png)

## Week 6 - Neural Networks
- [Traffic](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%206%20-%20Neural%20Networks): Used TensorFlow Keras to build convolutional neural networks to classify traffic signs. Loaded pictures of signs, standardized shapes and pixel intensity, and experimented with different amounts of hidden layers, convolution, pooling and dropout to achieve an image classification with 97% accuracy. See [here](https://github.com/JohnZolton/CS50_Artificial_Intelligence/blob/main/Week%206%20-%20Neural%20Networks/README.md) for an in-depth description of the testing process.

## Week 7 - Language
- [Parser](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%207%20-%20Language/parser): Used Natural Language Toolkit (NLTK) to parse a variety of sentences using Context-Free Grammar. In Context-Free Grammar, words are abstracted into nouns (N), verbs (V), adjectives (Adj) etc. and sentences are represented using syntax trees. Words were labelled as N, V, adj, adv and so on while rules were created for larger phrases like "the chair" -> "Determiner Noun" and "ran fast" -> "Verb Adverb". Sentences were processed and tokenized using NLTK, non-alphabet characters were filtered out and terminal noun phrases (a noun phrase without an internal noun phrase, ex: "the home" and not "the armchair in the home") were extracted.

![image](https://user-images.githubusercontent.com/102374100/189671285-30fbeedb-d4fd-439b-9065-125757061490.png)

- [Questions](https://github.com/JohnZolton/CS50_Artificial_Intelligence/tree/main/Week%207%20-%20Language/questions): Uses natural language processing and inverse document frequency to answer questions. When presented with a query (a question in English asked by the user), document retrieval will first identify which document(s) are most relevant to the query. Once the top documents are found, the top document(s) will be subdivided into passages (in this case, sentences) so that the most relevant passage to the question can be determined. To find relevant documents, all documents are ranked according to term frequency of the words (how often query words are in the document) and inverse document frequency (how rare the word is compared to the other documents). To find the relevant sentence, sentences in the document are ranked according to "matching word measure" (the sum off the inverse document frequencies for each query word, excluding repeats in the sentence). 
Files are loaded into a dictionary mapping filename to a string of its contents. Then the contents are tokenized usign NLTK and punctuation and stopwords (non-useful query words) are filtered out. Then IDF values are calculated for each document and relevant documents are selected. Finally, sentences are ranked according to relevance and the most relevant sentence is returned. 


![image](https://user-images.githubusercontent.com/102374100/190192398-0e3519d2-0a5f-47e2-b2f7-ed4ec3a54195.png)


![image](https://user-images.githubusercontent.com/102374100/190192475-05799eff-24d5-4c74-8c73-aace533abbac.png)


![image](https://user-images.githubusercontent.com/102374100/190192528-c75d7b21-51bf-4799-a038-faaddce4ebbe.png)

