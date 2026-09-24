import tasks
from task_base import evaluate


def test_quiz_wrong_answer_fails_without_reward():
    spec = tasks.TASK_SPECS["cabinet"]
    inventory = set()
    result = evaluate(spec, inventory, 1)
    assert not result.success
    assert result.feedback == "НЕВЕРНО!"
    assert result.add_items == set()
    assert inventory == set()


def test_quiz_right_answer_succeeds():
    spec = tasks.TASK_SPECS["cabinet"]
    result = evaluate(spec, set(), spec["correct"])
    assert result.success
    assert result.feedback == "ВЕРНО!"
    assert result.add_items == {"ключ"}


def test_take_without_required_item_fails():
    spec = tasks.TASK_SPECS["safe"]
    result = evaluate(spec, set(), 1)
    assert not result.success
    assert result.feedback == "У вас нет кода!"
    assert result.add_items == set()
    assert result.remove_items == set()


def test_take_with_required_item_trades():
    spec = tasks.TASK_SPECS["safe"]
    inventory = {"код от сейфа"}
    result = evaluate(spec, inventory, 1)
    assert result.success
    assert result.add_items == {"ЯБЛОКО"}
    assert result.remove_items == {"код от сейфа"}


def test_take_return_option_is_noop():
    spec = tasks.TASK_SPECS["safe"]
    inventory = set()
    result = evaluate(spec, inventory, 2)
    assert not result.success
    assert result.feedback is None
    assert result.add_items == set()
    assert result.remove_items == set()


def test_take_without_requirements_always_succeeds():
    spec = tasks.TASK_SPECS["bake"]
    result = evaluate(spec, set(), 1)
    assert result.success
    assert result.add_items == {"мука"}


def test_note_always_succeeds():
    spec = tasks.TASK_SPECS["letter"]
    result = evaluate(spec, set(), 1)
    assert result.success
    assert result.feedback is None


def test_ending_always_succeeds():
    spec = tasks.TASK_SPECS["finish"]
    result = evaluate(spec, set(), None)
    assert result.success


def test_exit_requires_both_items():
    spec = tasks.TASK_SPECS["exit"]
    result = evaluate(spec, {"отпечаток"}, 1)
    assert not result.success
    assert result.feedback == "У вас нет отпечатка или яблока!"


def test_exit_finishes_the_game():
    spec = tasks.TASK_SPECS["exit"]
    inventory = {"отпечаток", "ЯБЛОКО"}
    result = evaluate(spec, inventory, 1)
    assert result.success
    assert result.add_items == {"КОНЕЦ"}
    assert result.remove_items == {"отпечаток", "ЯБЛОКО"}