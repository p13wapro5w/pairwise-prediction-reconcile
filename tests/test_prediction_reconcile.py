import pytest
from net import prediction_reconcile as mod

CASES = [
    ("tick", 'm.tick_rate(60, 30) == approx(0.5)'),
    ("tick_same", 'm.tick_rate(30, 30) == approx(1.0)'),
    ("replay_lost", 'm.replay_count([1, 2, 3], True) == 3'),
    ("replay_ok", 'm.replay_count([1, 2, 3], False) == 2'),
    ("rollback", 'm.rollback_state({"a": 1}, {"a": 2}) == {"a": 2}'),
    ("lag", 'm.lag_compensation(200, 50) == 50'),
    ("lag_small", 'm.lag_compensation(40, 50) == 20'),
    ("bind", 'm.bind_vehicle((1, 2), (3, 4)) == ((1, 2), (3, 4))'),
    ("collision", 'm.predict_collision(2.0, 1.0) is False'),
    ("no_collision", 'm.predict_collision(1.0, 1.0) is True'),
    ("offset", 'm.clock_offset(10, 8) == 2'),
    ("dedupe", 'm.dedupe_inputs([3, 1, 3, 2]) == [1, 2, 3]'),
    ("threshold", 'm.correct_threshold(10, 5) == 20'),
    ("threshold_floor", 'm.correct_threshold(1, 5) == 5'),
    ("snapshot", 'm.snapshot_key(3, "v1") == "3:v1"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
