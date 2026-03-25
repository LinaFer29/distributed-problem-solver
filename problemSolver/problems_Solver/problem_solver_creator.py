from abc import ABC, abstractmethod
from .i_problem_solver import IProblemSolver

class ProblemSolverCreator(ABC):

    def problemSolver_management(self,data):
        problem_solver = self.create_problemSolver()
        results = problem_solver.compute_results(data)

        return results
        
    @abstractmethod
    def create_problemSolver(self) -> IProblemSolver:
        pass
