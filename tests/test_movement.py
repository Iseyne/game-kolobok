import config
import pygame
import kolobok


def _kolobok(x=100, y=100):
    return kolobok.Kolobok(sprite=None, x=x, y=y)


def test_movement_updates_position():
    player = _kolobok()
    player._Kolobok__horizontal_move_flag = 1
    player.move([])
    assert player.x == 100 + config.speed


def test_movement_blocked_by_restricted_zone():
    player = _kolobok()
    wall = pygame.Rect(110, 100, 50, 50)
    player._Kolobok__horizontal_move_flag = 1
    player.move([wall])
    assert player.x == 100
    assert player.y == 100


def test_boundary_clamp_reapplied():
    player = _kolobok(x=10, y=700)
    player.check_logic()
    assert player.x == config.boundary_left
    assert player.y == config.boundary_bottom


def test_boundary_clamp_top_left():
    player = _kolobok(x=800, y=-5)
    player.check_logic()
    assert player.x == config.boundary_right
    assert player.y == config.boundary_top


def test_index_restricted_zone():
    player = _kolobok()
    zones = [pygame.Rect(0, 0, 50, 50), pygame.Rect(100, 100, 50, 50)]
    assert player.index_restricted_zone(zones) == 1


def test_index_restricted_zone_none_when_free():
    player = _kolobok(x=300, y=300)
    zones = [pygame.Rect(0, 0, 50, 50), pygame.Rect(100, 100, 50, 50)]
    assert player.index_restricted_zone(zones) is None


def test_vertical_movement_blocked_by_restricted_zone():
    player = _kolobok()
    zone = pygame.Rect(100, 120, 50, 50)
    player._Kolobok__vertical_move_flag = 1
    player.move([zone])
    assert player.y == 100