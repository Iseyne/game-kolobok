from quest import Quest


def test_quest_first_call_returns_task_text():
    npc = Quest(False, "task", "result", {"мука"})
    inventory = set()
    assert npc.get_text(inventory, "торт") == "task"
    assert inventory == set()


def test_quest_completes_when_requirements_present():
    npc = Quest(False, "task", "result", {"мука"})
    inventory = {"мука"}
    npc.get_text(inventory, "торт")
    assert npc.get_text(inventory, "торт") == "result"
    assert inventory == {"торт"}


def test_quest_removes_consumed_items_only():
    extra = "ЯБЛОКО"
    npc = Quest(False, "task", "result", {"мука"})
    inventory = {"мука", extra}
    npc.get_text(inventory, "торт")
    npc.get_text(inventory, "торт")
    assert inventory == {extra, "торт"}


def test_quest_result_is_repeatable():
    npc = Quest(False, "task", "result", {"мука"})
    inventory = {"мука"}
    npc.get_text(inventory, "торт")
    npc.get_text(inventory, "торт")
    assert npc.get_text(inventory, "торт") == "result"
    assert inventory == {"торт"}


def test_quest_does_not_complete_without_requirements():
    npc = Quest(False, "task", "result", {"мука"})
    inventory = set()
    npc.get_text(inventory, "торт")
    assert npc.get_text(inventory, "торт") == "task"
    assert inventory == set()