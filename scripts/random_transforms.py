#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# add random transforms to selected items

import random

import modo
import modo.constants as c
from modo import Vector3

from h3d_utilites.scripts.h3d_utils import get_user_value

USERVAL_NAME_MOV_X = "h3d_rtf_mov_X"
USERVAL_NAME_MOV_Y = "h3d_rtf_mov_Y"
USERVAL_NAME_MOV_Z = "h3d_rtf_mov_Z"
USERVAL_NAME_ROT_X = "h3d_rtf_rot_X"
USERVAL_NAME_ROT_Y = "h3d_rtf_rot_Y"
USERVAL_NAME_ROT_Z = "h3d_rtf_rot_Z"
USERVAL_NAME_SCL_X = "h3d_rtf_scl_X"
USERVAL_NAME_SCL_Y = "h3d_rtf_scl_Y"
USERVAL_NAME_SCL_Z = "h3d_rtf_scl_Z"
USERVAL_NAME_ENABLE_MOVE = "h3d_rtf_move"
USERVAL_NAME_ENABLE_ROTATE = "h3d_rtf_rotate"
USERVAL_NAME_ENABLE_SCALE = "h3d_rtf_scale"
USERVAL_NAME_ENABLE_UNIFORM_SCALE = "h3d_rtf_uniform_scale"


def main():
    selected: list[modo.Item] = modo.Scene().selectedByType(
        itype=c.LOCATOR_TYPE, superType=True
    )
    if not selected:
        return

    is_move = get_user_value(USERVAL_NAME_ENABLE_MOVE)
    is_rotate = get_user_value(USERVAL_NAME_ENABLE_ROTATE)
    is_scale = get_user_value(USERVAL_NAME_ENABLE_SCALE)
    is_uniform_scl = get_user_value(USERVAL_NAME_ENABLE_UNIFORM_SCALE)

    random.seed()

    for item in selected:
        if is_move:
            variation = Vector3()
            variation.x = get_user_value(USERVAL_NAME_MOV_X)
            variation.y = get_user_value(USERVAL_NAME_MOV_Y)
            variation.z = get_user_value(USERVAL_NAME_MOV_Z)

            pos = Vector3(item.position.get())
            rnd_pos = randomize_additive(pos, variation)
            item.position.set(rnd_pos)

        if is_rotate:
            variation = Vector3()
            variation.x = get_user_value(USERVAL_NAME_ROT_X)
            variation.y = get_user_value(USERVAL_NAME_ROT_Y)
            variation.z = get_user_value(USERVAL_NAME_ROT_Z)

            rot = Vector3(item.rotation.get())
            rnd_rot = randomize_additive(rot, variation)
            item.rotation.set(rnd_rot)

        if is_scale:
            variation = Vector3()
            variation.x = get_user_value(USERVAL_NAME_SCL_X)
            variation.y = get_user_value(USERVAL_NAME_SCL_Y)
            variation.z = get_user_value(USERVAL_NAME_SCL_Z)

            scl = Vector3(item.scale.get())
            rnd_scl = randomize_multiplicative(scl, variation, is_uniform_scl)
            item.scale.set(rnd_scl)


def randomize_additive(transform: Vector3, variation: Vector3) -> Vector3:
    rnd_transform = Vector3()
    rnd_transform.x = shift_additive(transform.x, variation.x, random.random())
    rnd_transform.y = shift_additive(transform.y, variation.y, random.random())
    rnd_transform.z = shift_additive(transform.z, variation.z, random.random())

    return rnd_transform


def shift_additive(value: float, variation: float, factor: float) -> float:
    return value + 2 * variation * factor - variation


def randomize_multiplicative(
    transform: Vector3, variation: Vector3, uniform: bool
) -> Vector3:
    rnd_transform = Vector3()
    if not uniform:
        rnd_transform.x = shift_multiplicative(
            transform.x, variation.x, random.random()
        )
        rnd_transform.y = shift_multiplicative(
            transform.y, variation.y, random.random()
        )
        rnd_transform.z = shift_multiplicative(
            transform.z, variation.z, random.random()
        )
    else:
        variation_uniform = get_uniform(variation)
        random_uniform = random.random()
        rnd_transform.x = shift_multiplicative(
            transform.x, variation_uniform, random_uniform
        )
        rnd_transform.y = shift_multiplicative(
            transform.y, variation_uniform, random_uniform
        )
        rnd_transform.z = shift_multiplicative(
            transform.z, variation_uniform, random_uniform
        )

    return rnd_transform


def shift_multiplicative(value: float, variation: float, factor: float) -> float:
    max_value = value * (1 + variation)
    min_value = 1 / max_value

    return min_value + (max_value - min_value) * factor


def get_uniform(variation: Vector3) -> float:
    return max(*variation)


if __name__ == "__main__":
    main()
