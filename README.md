# CS50_Artificial_Intelligence
Harvard CS50's Introduction to Artificial Intelligence with Python

## Week 1 - Search
- degrees: uses a breadth-first search to find minimum degrees of separation between two actors (source and target) via their co-stars. Initializes the first actor as a node with their id and added their co-stars to the frontier. Then explores each movie's stars for the target star and repeats for each of their movies until it finds a connection. 
