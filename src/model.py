"""
Module: model.py
Description: This module contains the model function for the project.
"""

from typing import List

#def model(x: float, weight: float=2.0, intercept: float=0.0):
#    return weight * x + intercept

class Model:
    """
    Class Model

    Parameters
    ----------
    weight : float
        Weight of the model
    intercept : float
        Intercept of the model

    Returns
    -------
    Model
        A model object
    """
    def __init__(self, weight: float=2.0, intercept: float=0.0) -> None:
        """
        Constructor for Model class

        Parameters
        ----------
        weight : float
            Weight of the model
        intercept : float
            Intercept of the model

        Returns
        -------
        None
        """
        self.weight = weight
        self.intercept = intercept

    def calc(self, x: float) -> float:
        """
        Method to calculate the output of the model

        Parameters
        ----------
        x : float
            Input data

        Returns
        -------
        float
            Output data        
        """
        return self.weight * x + self.intercept

    def predict(self, data: List[float]) -> List[float]:
        """
        Method to predict the output of the model

        Parameters
        ----------
        data : List[float]
            Input data

        Returns
        -------
        List[float]
            Output data
        """
        return [self.calc(x_i) for x_i in data]
