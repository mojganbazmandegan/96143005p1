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
    
    #ایجاد یک پشته
    dfsstack=util.Stack()
    #ایجادیک لیست خالی برای گره های دیده شده یا همون کاوش شده
    dideshode=[]
    # گرفتن گره اغاز که همان نقطه 5,5 در تاینی میز است
    #قرار دادن ان در پشته
    startState=problem.getStartState()
    startNod=( startState,[])
    dfsstack.push(startNod)
    # تا زمانی ک پشته خالی نشده عملیات پیشایش اول عمق انجام بده و زمانی ک پشته خالی شد عملیات به پایان میرسد
    #و در پایان لیست اکشن ک همان مسیر پیدا شده توسط جستجوی اول عمق است برگردانده میشود
    while not dfsstack.isEmpty():
        currentStat,actions=dfsstack.pop()
        #درصورتی ک گره قبلا دیده نشده بود به لیست دیده شده ها اضافش کن
        if currentStat not in dideshode:
            dideshode.append(currentStat)
            """ اگه گره مورد نظر گره هدف بود حرکات رو برگردون و پایان  
              در غیر این صورت حرکات مجاز گره فعلی رو توسط تابع ساکسسور گرفته و توسط حلقه تمام حرکات مجاز 
              که در ساکسسور قرار دارن یکی پس از دیگری طبق الگوریتم اول عمق انجام داده و گره های حاصل رو
              به پشته اضافه میکنیم
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
    
    #ایجاد یک صف
    frontir=util.Queue()
    #ایجادیک لیست خالی برای گره های دیده شده یا همون کاوش شده
    explorednodes=[]
   
    # گرفتن گره اغاز که همان نقطه 5,5 در تاینی میز است
    #قرار دادن ان در پشته
    startState=problem.getStartState()
    startNod=( startState,[])
    frontir.push(startNod)
    # تا زمانی ک پشته خالی نشده عملیات پیمایش اول سطح انجام و زمانی ک پشته خالی شد عملیات به پایان میرسد
    #و در پایان لیست اکشن ک همان مسیر پیدا شده توسط جستجوی اول سطح است برگردانده میشود
    while not frontir.isEmpty():
        currentStat,actions=frontir.pop()
        
        #درصورتی ک گره قبلا دیده نشده بود به لیست دیده شده ها اضافش کن
        if currentStat not in explorednodes:
            explorednodes.append(currentStat)
            """ اگه گره مورد نظر گره هدف بود حرکات رو برگردون و پایان  
              در غیر این صورت حرکات مجاز گره فعلی رو توسط تابع ساکسسور گرفته و توسط حلقه تمام حرکات مجاز 
              که در ساکسسور قرار دارن یکی پس از دیگری طبق الگوریتم اول عمق انجام داده و گره های حاصل رو
              به صف اضافه میکنیم
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
    #گرفتن نقظه استارت
    start = problem.getStartState()
    #ساخت لیست برای نود های ویزیت شده
    exploredState = []
    #ساخت صف الویت چرا که در این الگوریتم بر اساس هزینه مسیر نود هارو از صف خارج میکنیم
    states = util.PriorityQueue()
    #درج حالت شروع در صف الویت
    states.push((start, []) ,0)

    # حلقه اصلی برنامه
    while not states.isEmpty():
        state, actions = states.pop()
        #اگر هدف بود بیاد پایان
        if problem.isGoalState(state):
            return actions
            """
             اگر نود جاری دیده نشده بود ساکسسور های مجازشو حساب میکنیم سپس مختصات حالت جاری رو میگیریم و

            
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
    #ساخت یک دیکشنری از نود های دیده شده
    visitsnode = {}
    #اکشن های مسیر یا همون لیستی ک در پایان مسیر حرکت رو در خود دارد
    action = []
    # یه صف الویت مخصوص برای این الگوریتم
    myqueue = util.PriorityQueue()
    # مجموعه ای که نود هارو با والدشون نگهداری میکنه
    parentsnode = {}
    #مجموعه ای برای نگهداری نود ها با هزینه هاشون
    cost = {}

    #گرفتن نود اغازین و اضافه کردنش به صف الویت
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
            #اگر حرکت یا همون ساکسسور جدید قبلا دیده نشده بود هزینه جدید رو بدست میاریم
            if elem[0] not in visitsnode.keys():
                print("elem(0):",elem[0])
                priority = node[2] + elem[2] + heuristic(elem[0], problem)
                """
                اگر در حین بست دادن گره های مختلف هزینه اسکسسور زودتر محاسبه شد و 
                اگرهزینه جدید از  قبلی بیشتر بود ک خب بست رو ادامه بده
                """
                if elem[0] in cost.keys():
                    if cost[elem[0]] <= priority:
                        continue
                #اگرهزینه جدید کمتر از هزینه قبل بود در صف اضافه بشه و هزینه و والد تغیر کنه
                myqueue.push((elem[0], elem[1], node[2] + elem[2]), priority)
                cost[elem[0]] = priority
                # نگهداری ساکسسور و والد اون
                parentsnode[elem[0]] = node[0]

    # پیدا کردن مسیر نگهداری
    while(node_sol in parentsnode.keys()):
        #پیدا کردن والد
        node_sol_prev = parentsnode[node_sol]
        #افزدن جهت 
        action.insert(0, visitsnode[node_sol])
        # رفتن به نود قبل
        node_sol = node_sol_prev

    return action



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
