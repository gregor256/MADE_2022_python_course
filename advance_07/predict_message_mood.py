"""predict"""
import random


class SomeModel:
    """predict"""

    def __init__(self, weight=0):
        self.weight = weight

    def predict(self, message: str) -> float:
        """predict"""
        bias = len(message) * self.weight
        return random.random() + bias

    def fit(self):
        """fit"""
        return self.weight ** 2


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    """predict"""
    current_model = model
    score = current_model.predict(message)
    if score < bad_thresholds:
        return 'неуд'
    if score > good_thresholds:
        return 'отл'
    return 'норм'
