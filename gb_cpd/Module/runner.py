import os

from gb_cpd.Method.run import runCMD

class Runner(object):
    def __init__(self) -> None:
        return

    @staticmethod
    def run(
        x: str,
        y: str,
        w: float = 0.0,
        l: float = 100.0,
        b: float = 0.7,
        g: float = 3.0,
        k: float = float('inf'),
    ) -> bool:
        '''
        x: source point cloud
        y: target point cloud
        w: omega, outlier probability
        l: lambda, deform length = sqrt(D/l)
        b: beta, deform smooth weight
        g: gamma, random point matching weight
        k: kappa, random mixing coeff
        '''
        return True
