#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# add random rotation local X axis to selected items

import random

import lx
import modo.constants as c
from modo import Scene, Item, Vector3

from h3d_utilites.scripts.h3d_utils import (
    get_user_value,
    Axis,
    item_rotate_local,
    item_get_rotation,
)

from h3d_random_transforms.scripts.random_transforms import (
    USERVAL_NAME_ROT_X,
    USERVAL_NAME_ROT_Y,
    USERVAL_NAME_ROT_Z,
    randomize_additive,
)


def main():
    args = lx.args()
    if not args:
        return

    selected: list[Item] = Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)
    if not selected:
        return

    command = {
        'X': Axis.X,
        'x': Axis.X,
        'Y': Axis.Y,
        'y': Axis.Y,
        'Z': Axis.Z,
        'z': Axis.Z,
    }

    axis = command.get(args[0], Axis.Y)
    variation = Vector3()
    variation.x = get_user_value(USERVAL_NAME_ROT_X)
    variation.y = get_user_value(USERVAL_NAME_ROT_Y)
    variation.z = get_user_value(USERVAL_NAME_ROT_Z)

    random.seed()
    for item in selected:
        rot = item_get_rotation(item)
        rnd_rot = randomize_additive(rot, variation)
        rotate_radians = {
            Axis.X: rnd_rot.x,
            Axis.Y: rnd_rot.y,
            Axis.Z: rnd_rot.z,
        }
        item_rotate_local(item, rotate_radians[axis], axis)


if __name__ == '__main__':
    main()
