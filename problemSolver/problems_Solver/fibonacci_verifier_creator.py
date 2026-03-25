from .i_problem_solver import IProblemSolver
from .problem_solver_creator import ProblemSolverCreator
from .fibonacci_verifier import FibonacciVerifier

class FibonacciVerifierCreator(ProblemSolverCreator):

    def create_problemSolver(self) -> IProblemSolver:
        return FibonacciVerifier()
