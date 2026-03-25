from .i_problem_solver import IProblemSolver
from .problem_solver_creator import ProblemSolverCreator
from .fizzbuzz import FizzBuzz

class FizzBuzzCreator(ProblemSolverCreator):

    def create_problemSolver(self) -> IProblemSolver:
        return FizzBuzz()
