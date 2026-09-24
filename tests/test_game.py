import config
import tasks
from app import is_game_finished
from quest import Quest
from task_base import evaluate


def test_is_game_finished():
    assert not is_game_finished(set())
    assert not is_game_finished({"ЯБЛОКО", "отпечаток"})
    assert is_game_finished({"КОНЕЦ"})
    assert is_game_finished({"КОНЕЦ", "ЯБЛОКО"})


def _npc_spec(name):
    for spec in config.NPC_DEFS:
        if spec["name"] == name:
            return spec
    raise KeyError(name)


def _talk(name, inventory):
    spec = _npc_spec(name)
    npc = Quest(False, spec["task_text"], spec["result_text"], spec["required_items"])
    reward = spec["reward"]
    npc.get_text(inventory, reward)
    npc.get_text(inventory, reward)
    return inventory


def _do(task_key, inventory, choice):
    result = evaluate(tasks.TASK_SPECS[task_key], inventory, choice)
    assert result.success, task_key
    inventory |= result.add_items
    inventory -= result.remove_items
    return inventory


def test_full_quest_chain_to_victory():
    inventory = set()

    _talk("volf", inventory)
    assert "морковь" in inventory

    _do("table", inventory, 1)
    assert "МЕЧ" in inventory

    _talk("fox", inventory)
    assert "отпечаток" in inventory

    _do("cabinet", inventory, 4)
    assert "ключ" in inventory

    _do("fridge", inventory, 1)
    assert "молоко" in inventory
    assert "ключ" not in inventory

    _do("bake", inventory, 1)
    assert "мука" in inventory

    _do("painting", inventory, 3)
    assert "яйца" in inventory

    _talk("medved", inventory)
    assert "торт" in inventory

    _talk("rabbit", inventory)
    assert "код от сейфа" in inventory

    _do("safe", inventory, 1)
    assert "ЯБЛОКО" in inventory
    assert "код от сейфа" not in inventory

    _do("exit", inventory, 1)
    assert is_game_finished(inventory)


def test_exit_does_not_finish_without_apple():
    inventory = {"отпечаток", "МЕЧ"}
    result = evaluate(tasks.TASK_SPECS["exit"], inventory, 1)
    assert not result.success
    assert not is_game_finished(inventory)


def test_medved_does_not_bake_without_ingredients():
    inventory = {"мука"}
    spec = _npc_spec("medved")
    npc = Quest(False, spec["task_text"], spec["result_text"], spec["required_items"])
    npc.get_text(inventory, "торт")
    npc.get_text(inventory, "торт")
    assert "торт" not in inventory