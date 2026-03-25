from .i_problem_solver import IProblemSolver
from .problem_solver_creator import ProblemSolverCreator
from .prime_classifier import PrimeClassifier

class PrimeClassifierCreator(ProblemSolverCreator):

    def create_problemSolver(self) -> IProblemSolver:
        return PrimeClassifier()
