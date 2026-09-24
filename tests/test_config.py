import os

import config
import tasks

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_npc_sprites_exist():
    for spec in config.NPC_DEFS:
        path = os.path.join(PROJECT_ROOT, spec["sprite"])
        assert os.path.exists(path), spec["sprite"]


def test_furniture_sprites_exist():
    for spec in config.FURNITURE:
        path = os.path.join(PROJECT_ROOT, spec["sprite"])
        assert os.path.exists(path), spec["sprite"]


def test_scene_sprites_exist():
    for name, spec in tasks.TASK_SPECS.items():
        bg = spec.get("bg")
        if bg is not None:
            path = os.path.join(PROJECT_ROOT, bg)
            assert os.path.exists(path), "%s -> %s" % (name, bg)


def test_furniture_task_keys_exist():
    for spec in config.FURNITURE:
        assert spec["task"] in tasks.TASK_SPECS


def test_quiz_correct_answers_are_in_range():
    for name, spec in tasks.TASK_SPECS.items():
        if spec["type"] == "quiz":
            assert 1 <= spec["correct"] <= len(spec["options"]), name


def test_known_task_types_only():
    known = {"note", "ending", "quiz", "take"}
    for name, spec in tasks.TASK_SPECS.items():
        assert spec["type"] in known, name


def test_finish_task_has_message():
    spec = tasks.TASK_SPECS["finish"]
    assert spec["type"] == "ending"
    assert spec["message"]


def test_npc_required_items_are_words():
    for spec in config.NPC_DEFS:
        assert spec["reward"]
        assert isinstance(spec["required_items"], set)