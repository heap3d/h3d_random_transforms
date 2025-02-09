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
        pos = modo.Vector3(item.position.get())
        rot = modo.Vector3(item.rotation.get())
        scl = modo.Vector3(item.scale.get())

        if is_move:
            range = modo.Vector3()
            range.x = get_user_value(USERVAL_NAME_MOV_X)
            range.y = get_user_value(USERVAL_NAME_MOV_Y)
            range.z = get_user_value(USERVAL_NAME_MOV_Z)

            rnd_pos = modo.Vector3()
            rnd_pos.x = pos.x + (random.random() * range.x) - range.x / 2
            rnd_pos.y = pos.y + (random.random() * range.y) - range.y / 2
            rnd_pos.z = pos.z + (random.random() * range.z) - range.z / 2
            item.position.set(rnd_pos)

        if is_rotate:
            range = modo.Vector3()
            range.x = get_user_value(USERVAL_NAME_ROT_X)
            range.y = get_user_value(USERVAL_NAME_ROT_Y)
            range.z = get_user_value(USERVAL_NAME_ROT_Z)

            rnd_rot = modo.Vector3()
            rnd_rot.x = rot.x + (random.random() * range.x) - range.x / 2
            rnd_rot.y = rot.y + (random.random() * range.y) - range.y / 2
            rnd_rot.z = rot.z + (random.random() * range.z) - range.z / 2
            item.rotation.set(rnd_rot)

        if is_scale:
            range = modo.Vector3()
            range.x = get_user_value(USERVAL_NAME_SCL_X)
            range.y = get_user_value(USERVAL_NAME_SCL_Y)
            range.z = get_user_value(USERVAL_NAME_SCL_Z)

            rnd_scl = modo.Vector3()
            if not is_uniform_scl:
                rnd_scl.x = scl.x + scl.x * ((random.random() * range.x) - range.x / 2)
                rnd_scl.y = scl.y + scl.y * ((random.random() * range.y) - range.y / 2)
                rnd_scl.z = scl.z + scl.z * ((random.random() * range.z) - range.z / 2)
            else:
                uniscale = max(*range)
                rnd_num = random.random()
                rnd_scl.x = scl.x + scl.x * ((rnd_num * uniscale) - uniscale / 2)
                rnd_scl.y = rnd_scl.x
                rnd_scl.z = rnd_scl.x

            item.scale.set(rnd_scl)


if __name__ == "__main__":
    main()
