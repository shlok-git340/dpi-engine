from sklearn.ensemble import IsolationForest
import numpy as np


class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(
            contamination=0.05
        )

        # Dummy bootstrap training
        dummy_data = np.array([
            [10, 1000, 0],
            [15, 2000, 0],
            [20, 3000, 0],
            [1000, 999999, 1]
        ])

        self.model.fit(dummy_data)

    def predict(self, X):
        return self.model.predict(X)