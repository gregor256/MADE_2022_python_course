"""test"""
from unittest import mock
import pytest
from predict_message_mood import predict_message_mood, SomeModel


@pytest.mark.parametrize(
    "message, score, expected",
    [
        ('gg', 0.1, 'неуд'),
        ('wp', 0.5, 'норм'),
        ('gl', 0.9, 'отл')
    ],
)
def test_predict_message_mood(message, score, expected):
    """test"""
    with mock.patch("predict_message_mood.SomeModel.predict") as mock_predict:
        mock_predict.return_value = score

        assert predict_message_mood(message, SomeModel()) == expected


def test_predict_message_mood_raises():
    """test"""
    with pytest.raises(TypeError) as exc_info:
        predict_message_mood(1, SomeModel())
    assert str(exc_info.value) == "object of type 'int' has no len()"
