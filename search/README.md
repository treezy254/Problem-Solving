# Problem-solving-search
Searching algorithms using python

agent - entity that percives its environment and acts upon that environment

state - a configuration of the agent and its environment

intital state - where to begin

action - choices that can be made in a state

actions(s) - return the set of actons that can bes executed in steps s

Transition Model - a description of what state results from performing any applicable action in any state

Result(S, a) -> returns the state resulting from perfoming action a in state s

state space - the set of all states reachable from the initial state by any sequence of actions

goal test - way to determine whether a given state is a goal state

path cost - numerical cost associated 

node : a data structure that keeps track of
	- a state
	- a parent (node that generated this node)
	- an action (action applied to parent to get node)
	- a path cost (from initial state to node)

## Approah
<ol>
	<li>Start with a frontier that contains the initial state</li>
<li>repeat:</li>
	<ul>
	<li>if the frontier is empty, then no solution</li>
	<li>a node from the frontier</li>
	<li>if node contains goal state, return the solution</li>
	<li>expand node, add resulting nodes to the frontier if they aren't already in the frontier or the explored set</li>
	</ul>
</ol>
<strong>Stack</strong> : last-in forst-out data type

<strong>depth-first search</strong> : search algorithm that always expands the deepest node in the frontier

<strong>Queue</strong> : first-in first-out data type

<strong>Breadth-first search</strong> : search algorithm that always expands the shallowest node in the frontier



<strong>Informed search</strong> : search strategy that uses problem-specific knowledge to find solutions more efficiently

	1. Greedy best-first search
		- search algorithm that expands the node that is closest to the goal, as estimated by a heuristic function h(n)

	2. A* search :
		- search algorithm that expands node with lowest value of g(n) + h(n)

		g(n) = cost to reach node
		h(n) = estimated cost to goal

		optimal if:
			- h(n) is admissible (never overestimate the true cost), and
			- h(n) is consistent (for every node n and successor n' with step cost c, h(n) <= h(n')+c)

		
	3. Min-max :
		given a state s:
			- MAX picks action a in Actions(s) that produces highest value of Min-VALUE(RESULT(s, a))
			- MIN picks action a in ACTIONS(s) that produces smallest value of MAX_VALUE(RESULTS(s, a))

		function MAX_VALUE(State):
		if TERMINAL(sate):
			return UTILITY(state)
		v = -infinity
		for action in ACTIONS(state):
			v = MAX(v, MIN_VALUE(RESULT(state, action)))
		return v

	4. Alpha-Beta Pruning :
		- smart min-max

	5. Depth-Limited Minimax :
		- Chess
