#!/usr/bin/python
# ================================
# (C)2025 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# add random transforms to selected items

import modo
import modo.constants as c


def main():
    selected = modo.Scene().selectedByType(itype=c.LOCATOR_TYPE, superType=True)


if __name__ == '__main__':
    main()
