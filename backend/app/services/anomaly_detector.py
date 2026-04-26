import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from ..models.models import LogEntry

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self.is_trained = False

    def train(self, data: pd.DataFrame):
        # In a real scenario, we'd extract features like log frequency, length, etc.
        # Here we just use log message length as a dummy feature
        features = self._extract_features(data)
        self.model.fit(features)
        self.is_trained = True

    def predict(self, log: LogEntry) -> bool:
        if not self.is_trained:
            return False
        
        feature = np.array([[len(log.message)]])
        prediction = self.model.predict(feature)
        return prediction[0] == -1 # -1 means anomaly

    def _extract_features(self, data: pd.DataFrame):
        # Simple feature: message length
        return data['message'].apply(len).values.reshape(-1, 1)

anomaly_detector = AnomalyDetector()
