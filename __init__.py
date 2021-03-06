# -*- coding: utf-8 -*-
"""This file is part of the libsigrokdecode project.

Copyright (C) 2019 Libor Gabaj <libor.gabaj@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

DECODER:
This decoder stacks on top of the ``tmc`` protocol decoder and decodes
the display driver TM1638 controlling up to 8 pcs of 7-segment digits with
decimal points, up to 8 two-color LEDs, and up to 24 keys scanning.

NOTE:
The decoder has been tested on display modules with following configurations:
- 8 digital tubes
- 8 digital tubes, 8 red LEDs, 8 keys
- 8 digital tubes, 8 red&green LEDs, 8 keys

All those modules have digital tubes connected to even display addresses
(counting from 0), i.e., 0x00, 0x02, ..., 0x0E, and LED to odd addresses, i.e.,
0x01, 0x03, ..., 0x0F.

Bit 0 (register value 0x01) of an LED address turns on a red LED.
It is equivalent to segment "a" of a digital tube.
Bit 1 (register value 0x02) of an LED address turns on a green LED.
It is equivalent to segment "b" of a digital tube.
Both colors of an LED cannot be turned on at once just the last of them.

Key scan bits K1 ~ K3 and nibbles KS1 ~ KS8 are mapped to physical switches
S1 - S24. Only a modul with 8 keys has been tested.

"""

from .pd import Decoder
