# CS50Ai 2023

## 10/17/2023
Search
Knowledge - We want our Ai to know, represent, and draw inferences from information. 
Uncertainty - What happens when a computer isn't sure about a fact but a probability. 
Optimization - Problems of when the computer is trying to optimize for a certain goal. 
Learning - Learning from data and experience; perform a task greater and greater. 
Neural Networks - Draw inspiration from human intelligence
Language - Human language; challenges of computer trying to understand natural language

### Search Problems
15 Puzzle; Solving a maze

== Terminology == 
[Agent] - Entity that perceives its environment and acts upon that environment. 
Ex. The agent will be the car that is trying to get from point A to point B

[State] - A configuration of the agent in th environment. 
[Actions] - Choices that can be made in a state
[transition model] - A description of what state results from performing any action in a state 
I.e. Results(s, a) - return the state resulting from performing action a in state s
[State Space] - the set of all states reachable from the initial state 
[Goal test] - Way to determine whether a given state is a goal state
[Path cost] - Numerical cost associated with a given path
[Optimal Solution] - a solutation has the lowest path cost among all solutions.

[Node] - a date structure that keeps track of 
    - a state
    - a parent (node generated this node)
    - an action (action applied to parent to get node)
    - a path cost (from initial state to node)

== Approach == 
    - Start with a frontier that contains the initial state
    - Repeat:
        - if the frontier is empty, then no solution. 
        - remove a node from the frontier
        - if node contains goal state, return the solution
        - Expand node, add resulting nodes to the frontier

Sample problem
Find a path from A to E

Defining an "Explored State" to contain nodes of states that we have already explored to prevent 
backtracking on progress i.e. A to B to A infinite loop.

[Stack] - LIFO data structure

[Depth-first search] - Search algorithm that always expands the deepest node in the frontier
    - Will use stack - LIFO
[breadth-first search] - Search algorithm that always expands the shallowest node in the frontier
    - Will use queue - FIFO

breadth first search was able to find optimal solution in a maze problem

Inheriting functions from another python class
```
def newclass(inheritedclass)
```

[Uninformed search] - Search strategy that uses no problem specific knowledge (Algorithms above)
[informed search] - Search strategy that uses problem-specific knowledge to find solutions more efficiently

Greedy best-first search - Search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n).

Heuristic function - takes a state as input and returns closeness to a goal
Manhattan distance - no diagonals, subtract x and y values from each other to estimate how close something is to the goal.

A* search - search algorithm that expands node with lowest value of g(n) + h(n)

g(n) = cost to reach node
h(n) = estimated cost to goal

optimal if:
    - h(n) is admissible (never overestimates the true cost), and 
    - h(n) is consistent (for every node n and successor n' with step cost c, h(n) <_ h(n') + c)

Adversarial Search
I.e. Tic Tac Toe

[Minimax Algorithm] 
    - -1 (O wins), 0 (nobody wins), 1 (X wins)
    - MAX(X) aims to maximize score
    - MIN(O) aims to minimize score
    - Given a state s:
        - MAX picks action a in ACTIONS(s) that produces highest value of MIN-value(RESUL(s,a))
        - MIN picks action a in ACTIONS(s) that produces smallest value  of Max-Value(RESULT(s,a))

Game
    - So: Initial state
    - Player(s): returns which player to move in state s
    - ACTION(s): return legal moves in state s
    - RESULTS(S, a) returns state after action a taken in state s
    - Terminal(s): Checks if state s is a terminal state
    - utility(s): Final numerical value for terminal state s

Optimizations
[Alpha-Bet pruning] - Keeping track of best and worst case scores as you are calculating paths
[Depth-limited minimax] - After a certain amount of moves, I'm going to stop and not consider additional moves due to computational requirements
    - Evaluation function - function that estimates the expected utility of a game from a state








