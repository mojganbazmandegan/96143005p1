# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    
    #?????????? ???? ????????
    dfsstack=util.Stack()
    #?????????????? ???????? ???????? ???????? ?????? ?????? ???????? ?????? ???? ???????? ???????? ??????
    dideshode=[]
    # ?????????? ?????? ???????? ???? ???????? ???????? 5,5 ???? ?????????? ?????? ??????
    #???????? ???????? ???? ???? ????????
    startState=problem.getStartState()
    startNod=( startState,[])
    dfsstack.push(startNod)
    # ???? ?????????? ?? ???????? ???????? ???????? ???????????? ???????????? ?????? ?????? ?????????? ?????? ?? ?????????? ?? ???????? ???????? ???? ???????????? ???? ?????????? ??????????
    #?? ???? ?????????? ???????? ???????? ?? ???????? ???????? ???????? ?????? ???????? ???????????? ?????? ?????? ?????? ?????????????????? ??????????
    while not dfsstack.isEmpty():
        currentStat,actions=dfsstack.pop()
        #?????????????? ?? ?????? ???????? ???????? ???????? ?????? ???? ???????? ???????? ?????? ???? ?????????? ????
        if currentStat not in dideshode:
            dideshode.append(currentStat)
            """ ?????? ?????? ???????? ?????? ?????? ?????? ?????? ?????????? ???? ?????????????? ?? ??????????  
              ???? ?????? ?????? ???????? ?????????? ???????? ?????? ???????? ???? ???????? ???????? ?????????????? ?????????? ?? ???????? ???????? ???????? ?????????? ???????? 
              ???? ???? ?????????????? ???????? ???????? ?????? ???? ???? ?????????? ?????? ???????????????? ?????? ?????? ?????????? ???????? ?? ?????? ?????? ???????? ????
              ???? ???????? ?????????? ????????????
             """
            if problem.isGoalState(currentStat):
                return actions
            else:
                successors=problem.getSuccessors(currentStat)
               
                for succst,sucact,succcost in successors:
                    
                    newAct=actions+[sucact]
                    newNod=(succst,newAct)
                    if not succst in dideshode:
                     dfsstack.push(newNod)
    return actions 
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    #?????????? ???? ????
    frontir=util.Queue()
    #?????????????? ???????? ???????? ???????? ?????? ?????? ???????? ?????? ???? ???????? ???????? ??????
    explorednodes=[]
   
    # ?????????? ?????? ???????? ???? ???????? ???????? 5,5 ???? ?????????? ?????? ??????
    #???????? ???????? ???? ???? ????????
    startState=problem.getStartState()
    startNod=( startState,[])
    frontir.push(startNod)
    # ???? ?????????? ?? ???????? ???????? ???????? ???????????? ???????????? ?????? ?????? ?????????? ?? ?????????? ?? ???????? ???????? ???? ???????????? ???? ?????????? ??????????
    #?? ???? ?????????? ???????? ???????? ?? ???????? ???????? ???????? ?????? ???????? ???????????? ?????? ?????? ?????? ?????????????????? ??????????
    while not frontir.isEmpty():
        currentStat,actions=frontir.pop()
        
        #?????????????? ?? ?????? ???????? ???????? ???????? ?????? ???? ???????? ???????? ?????? ???? ?????????? ????
        if currentStat not in explorednodes:
            explorednodes.append(currentStat)
            """ ?????? ?????? ???????? ?????? ?????? ?????? ?????? ?????????? ???? ?????????????? ?? ??????????  
              ???? ?????? ?????? ???????? ?????????? ???????? ?????? ???????? ???? ???????? ???????? ?????????????? ?????????? ?? ???????? ???????? ???????? ?????????? ???????? 
              ???? ???? ?????????????? ???????? ???????? ?????? ???? ???? ?????????? ?????? ???????????????? ?????? ?????? ?????????? ???????? ?? ?????? ?????? ???????? ????
              ???? ???? ?????????? ????????????
             """
            if problem.isGoalState(currentStat):
                return actions
            else:
                successors=problem.getSuccessors(currentStat)
                print("suc:",successors)

                for succst,sucact,succcost in successors:
                    
                    newAct=actions+[sucact]
                    newNod=(succst,newAct)
                    if not succst in explorednodes:
                     frontir.push(newNod)
    return actions            

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #?????????? ???????? ????????????
    start = problem.getStartState()
    #???????? ???????? ???????? ?????? ?????? ?????????? ??????
    exploredState = []
    #???????? ???? ?????????? ?????? ???? ???? ?????? ???????????????? ???? ???????? ?????????? ???????? ?????? ???????? ???? ???? ???????? ????????????
    states = util.PriorityQueue()
    #?????? ???????? ???????? ???? ???? ??????????
    states.push((start, []) ,0)

    # ???????? ???????? ????????????
    while not states.isEmpty():
        state, actions = states.pop()
        #?????? ?????? ?????? ???????? ??????????
        if problem.isGoalState(state):
            return actions
            """
             ?????? ?????? ???????? ???????? ???????? ?????? ?????????????? ?????? ???????????? ???????? ???????????? ?????? ???????????? ???????? ???????? ???? ?????????????? ??

            
            """
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            print("sucsseors:",successors)
            for succ in successors:
                sucstat = succ[0]
                if sucstat not in exploredState:
                    directions = succ[1]
                    newCost = actions + [directions]
                    print(problem.getCostOfActions(newCost))
                    states.push((sucstat, actions + [directions]), problem.getCostOfActions(newCost))
        exploredState.append(state)
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #???????? ???? ?????????????? ???? ?????? ?????? ???????? ??????
    visitsnode = {}
    #???????? ?????? ???????? ???? ???????? ?????????? ?? ???? ?????????? ???????? ???????? ???? ???? ?????? ????????
    action = []
    # ???? ???? ?????????? ?????????? ???????? ?????? ????????????????
    myqueue = util.PriorityQueue()
    # ???????????? ???? ???? ?????? ???????? ???? ?????????????? ?????????????? ??????????
    parentsnode = {}
    #???????????? ???? ???????? ?????????????? ?????? ???? ???? ?????????? ??????????
    cost = {}

    #?????????? ?????? ???????????? ?? ?????????? ?????????? ???? ???? ??????????
    start = problem.getStartState()
    myqueue.push((start, 'Undefined', 0), 0)
    visitsnode[start] = 'Undefined'
    cost[start] = 0
    goal = False;



    while(not myqueue.isEmpty() and goal != True):
        node = myqueue.pop()
        visitsnode[node[0]] = node[1]
        if problem.isGoalState(node[0]):
            node_sol = node[0]
            goal = True
            break

        for elem in problem.getSuccessors(node[0]):
            #?????? ???????? ???? ???????? ?????????????? ???????? ???????? ???????? ???????? ?????? ?????????? ???????? ???? ???????? ????????????
            if elem[0] not in visitsnode.keys():
                print("elem(0):",elem[0])
                priority = node[2] + elem[2] + heuristic(elem[0], problem)
                """
                ?????? ???? ?????? ?????? ???????? ?????? ?????? ?????????? ?????????? ?????????????? ?????????? ???????????? ???? ?? 
                ???????????????? ???????? ????  ???????? ?????????? ?????? ?? ???? ?????? ???? ?????????? ??????
                """
                if elem[0] in cost.keys():
                    if cost[elem[0]] <= priority:
                        continue
                #???????????????? ???????? ???????? ???? ?????????? ?????? ?????? ???? ???? ?????????? ?????? ?? ?????????? ?? ???????? ???????? ??????
                myqueue.push((elem[0], elem[1], node[2] + elem[2]), priority)
                cost[elem[0]] = priority
                # ?????????????? ?????????????? ?? ???????? ??????
                parentsnode[elem[0]] = node[0]

    # ???????? ???????? ???????? ??????????????
    while(node_sol in parentsnode.keys()):
        #???????? ???????? ????????
        node_sol_prev = parentsnode[node_sol]
        #?????????? ?????? 
        action.insert(0, visitsnode[node_sol])
        # ???????? ???? ?????? ??????
        node_sol = node_sol_prev

    return action



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
