import copy

#import json
# import numpy as np  # contains helpful math functions like numpy.exp()
# import numpy.random as random  # see numpy.random module

import math
import random  # alternative to numpy.random module
#
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# #%matplotlib inline


class TravelingSalesmanProblem:
    """Representation of a traveling salesman optimization problem.  The goal
    is to find the shortest path that visits every city in a closed loop path.

    Students should only need to implement or modify the successors() and
    get_values() methods.

    Parameters
    ----------
    cities : list
        A list of cities specified by a tuple containing the name and the x, y
        location of the city on a grid. e.g., ("Atlanta", (585.6, 376.8))

    Attributes
    ----------
    names
    coords
    path : list
        The current path between cities as specified by the order of the city
        tuples in the list.
    """

    def __init__(self, cities):
        self.path = copy.deepcopy(cities)

    def copy(self):
        """Return a copy of the current board state."""
        new_tsp = TravelingSalesmanProblem(self.path)
        return new_tsp

    @property
    def names(self):
        """Strip and return only the city name from each element of the
        path list. For example,
            [("Atlanta", (585.6, 376.8)), ...] -> ["Atlanta", ...]
        """
        names, _ = zip(*self.path)
        return names

    @property
    def coords(self):
        """Strip the city name from each element of the path list and return
        a list of tuples containing only pairs of xy coordinates for the
        cities. For example,
            [("Atlanta", (585.6, 376.8)), ...] -> [(585.6, 376.8), ...]
        """
        _, coords = zip(*self.path)
        return coords

    def successors(self):
        """Return a list of states in the neighborhood of the current state by
        switching the order in which any adjacent pair of cities is visited.

        For example, if the current list of cities (i.e., the path) is [A, B, C, D]
        then the neighbors will include [A, B, D, C], [A, C, B, D], [B, A, C, D],
        and [D, B, C, A]. (The order of successors does not matter.)

        In general, a path of N cities will have N neighbors (note that path wraps
        around the end of the list between the first and last cities).

        l = len(self.path)
        res = []
        for i in range(l):
            succ = self.copy()
            succ.path[i], succ.path[(i+1)%l] = succ.path[(i+1)%l], succ.path[i]
            res.append(succ)
        return res

        """
        l = len(self.path)

        def nxt(i):
            succ = self.copy()
            succ.path[i], succ.path[(i+1)%l] = succ.path[(i+1)%l], succ.path[i]
            return succ

        return [nxt(i) for i in range(l)]


    def get_value(self):
        """Calculate the total length of the closed-circuit path of the current
        state by summing the distance between every pair of adjacent cities.  Since
        the default simulated annealing algorithm seeks to maximize the objective
        function, return -1x the path length. (Multiplying by -1 makes the smallest
        path the smallest negative number, which is the maximum value.)

        Notes
        -----
            (1) Remember to include the edge from the last city back to the
            first city

            (2) Remember to multiply the path length by -1 so that simulated
            annealing finds the shortest path
        """
        from math import sqrt
        l = len(self.path)
        # euclidian distance between two cities
        return -sum([(lambda ci, cj: sqrt((ci[0] - cj[0])**2 + (ci[1] - cj[1])**2))
                     (self.coords[i], self.coords[(i+1) % l]) for i in range(l)])


alpha = 0.95
temperature=1e4


def exp_schedule(k=20, lam=0.05, limit=100):
    import math
    "One possible schedule function for simulated annealing"
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)


def schedule(t):
    """
    The most common temperature schedule is simple exponential decay:  T(t)=αtT0

    (Note that this is equivalent to the incremental form  Ti+1=αTi,
    but implementing that form is slightly more complicated because you need to preserve state between calls.)
    In most cases, the valid range for temperature  T0
      can be very high (e.g., 1e8 or higher), and the decay parameter  α
      should be close to, but less than 1.0 (e.g., 0.95 or 0.99).
      Think about the ways these parameters effect the simulated annealing function.
      Try experimenting with both parameters to see how it changes runtime and the quality of solutions.
    """
    import math
    res = temperature * math.pow(alpha, t)
    return res


def simulated_annealing(problem, schedule):
    """The simulated annealing algorithm, a version of stochastic hill climbing
    where some downhill moves are allowed. Downhill moves are accepted readily
    early in the annealing schedule and then less often as time goes on. The
    schedule input determines the value of the temperature T as a function of
    time. [Norvig, AIMA Chapter 3]

    Parameters
    ----------
    problem : Problem
        An optimization problem, already initialized to a random starting state.
        The Problem class interface must implement a callable method
        "successors()" which returns states in the neighborhood of the current
        state, and a callable function "get_value()" which returns a fitness
        score for the state. (See the `TravelingSalesmanProblem` class below
        for details.)

    schedule : callable
        A function mapping time to "temperature". "Time" is equivalent in this
        case to the number of loop iterations.

    Returns
    -------
    Problem
        An approximate solution state of the optimization problem

    Notes
    -----
        (1) DO NOT include the MAKE-NODE line from the AIMA pseudocode

        (2) Modify the termination condition to return when the temperature
        falls below some reasonable minimum value (e.g., 1e-10) rather than
        testing for exact equality to zero

    See Also
    --------
    AIMA simulated_annealing() pseudocode
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Simulated-Annealing.md

    function SIMULATED-ANNEALING(problem,schedule) returns a solution state
     inputs: problem, a problem
     schedule, a mapping from time to "temperature"

     current ← MAKE-NODE(problem.INITIAL-STATE)
     for t = 1 to ∞ do
       T ← schedule(t)
       if T = 0 then return current
       next ← a randomly selected successor of current
       ΔE ← next.VALUE - current.VALUE
       if ΔE > 0 then current ← next
       else current ← next only with probability eΔE/T

        neighbors = current.expand(problem)
        if not neighbors:
            return current
        next = random.choice(neighbors)
        delta_e = problem.value(next.state) - problem.value(current.state)
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            current = next


    """
    iteration = 1
    done = False
    term_temp = 1e-10
    eps = 1e-3

    while not done:
        temp = schedule(iteration)
        #print(f"temperature {temp}")
        if temp < term_temp:
            return problem
        iteration += 1
        #print(f"iteration {iteration}")
        neighbors = problem.successors()
        next_state = random.choice(neighbors)
        delta_e = float(next_state.get_value()) - float(problem.get_value())
        #print(f"delta_e {delta_e}")
        if delta_e > 0.:
            problem = next_state
            continue
        xp = math.exp(delta_e / temp)
        r = random.random()
        #print(f"xp {xp}, r {r}")
        if abs(xp-r) <= eps:
            #print(f"JUMP to next state")
            problem = next_state


def test():

    # Construct an instance of the TravelingSalesmanProblem
    test_cities = [('DC', (11, 1)), ('SF', (0, 0)), ('PHX', (2, -3)), ('LA', (0, -4))]
    tsp = TravelingSalesmanProblem(test_cities)
    # print(tsp.path)
    assert(tsp.path == test_cities)

    # Test the successors() method -- no output means the test passed
    successor_paths = [x.path for x in tsp.successors()]
    assert(all(x in [[('LA', (0, -4)), ('SF', (0, 0)), ('PHX', (2, -3)), ('DC', (11, 1))],
                     [('SF', (0, 0)), ('DC', (11, 1)), ('PHX', (2, -3)), ('LA', (0, -4))],
                     [('DC', (11, 1)), ('PHX', (2, -3)), ('SF', (0, 0)), ('LA', (0, -4))],
                     [('DC', (11, 1)), ('SF', (0, 0)), ('LA', (0, -4)), ('PHX', (2, -3))]]
              for x in successor_paths))

    # # Test the get_value() method -- no output means the test passed
    # assert(np.allclose(tsp.get_value(), -28.97, atol=1e-3))
    # d = tsp.get_value()
    # print(d)

    # assert (np.allclose(schedule(0), temperature, atol=1e-3))
    # assert (np.allclose(schedule(10), 5987.3694, atol=1e-3))
    # print(temperature)
    # print(schedule(0))
    # print(schedule(10))

    sol = simulated_annealing(tsp, schedule)
    print(sol.path)

if __name__ == '__main__':
    test()