# Copyright (c) 2025 Frank David Martínez Muñoz <mnesarco>
# SPDX-License-Identifier: MIT

# fmt: off

# Import zkeymap language artifacts
from zkeymap.lang import (
    alias,
    layer,
    label,
    combo,
    uc_linux_shift_ctrl_u as uc,
    macro,
)

from zkeymap import     (
    keys,   # Import base key definitions  # noqa: F401
    keys_la, # Import Language specific keys (Latam) # noqa: F401
)

# Import or define a physical layout
from zkeymap.layouts import marz_split_3x6_4
layout = marz_split_3x6_4.layout


# User defined aliases
alias / "cw" / "&caps_word" / label("⇪")
alias / "zw" / "LC(LA(DOWN))"  # Windows Zoom (Linux Mint)
alias / "∴" / uc(name="t3p", char="∴", shifted="△")  # Fancy unicode chars

# Layers -----------------

layer / "def" / label("DEF") / r"""
    {⌘ esc}    q     w   f   p   b          j   l   u   y   acut     ñ
    {⎇ tab}  {⇧ a}   r   s   t   g          m   n   e   i   {⇧ o}   cw
    {⎈  \ }    z     x   c   d   v          k   h   ,   .     ;      ⏎

    (num tab) (sym ⌫) (nav ␣) [⇧ ⎇]         [r⎇] (nav ␣) (sym ⌫) (adj del)
    """

layer / "num" / label("NUM") / r"""
    ▽   *   7   8   9   /         /   7   8   9   *   ∴
    ,   0   4   5   6   -         -   4   5   6   0   ,
    zw  .   1   2   3   +         +   1   2   3   .   ▽

          ▽ (fc0 /) ▽   ▽         ▽   ▽   ▽   ▽
    """

layer / "sym" / label("SYM1") / r"""
    |      !   "  [#]  $   %       &     /    [ [ ]  [ \] ]    =     ?
    grv    *   '   :   _   -       -   [ ( ]  [ ) ]  [ {  ]  [ } ]   ▽
    diae   @   ~   ^   =   +       +     '    [ < ]  [ >  ]  [ \ ]   ▽

            (adj)  ▽   ▽   ▽       ▽  ▽  (num ~) ▽
    """

layer / "nav" / label("NAV") / r"""
    ▽  f1  f2  f3  f4  f5       ▽         [ pgup ]  [  ↑  ]  [ pgdn ]  [  f10 ]  [ f11 ]
    ▽  ⇧   '   :   _   -        [ home ]  [   ←  ]  [  ↓  ]  [   →  ]  [  end ]  [ f12 ]
    ▽  f6  f7  f8  f9  f10      [⎈ home]  [ ⎈ ←  ]   xxxxx   [ ⎈ →  ]  [⎈ end ]     ▽

                   ▽ ▽ ▽ ▽     ▽ ▽ ▽ ▽
    """

layer / "adj" / label("ADJ") / r"""
    ⚙      ▽     ▽     ▽   ▽   ▽      ▽   ▽   ▽   ▽   ▽   ⚙
    ᛒclr   ᛒ0    ᛒ1    ᛒ2  ᛒ3  ᛒ4     ᛒ4  ᛒ3  ᛒ2  ᛒ1  ᛒ0  ᛒclr
    ▽      nlck  usb/ᛒ ▽   ▽   ▽      ▽   ▽   ▽   ▽   ▽   ▽

                         ▽ ▽ ▽ ▽      ▽ ▽ ▽ ▽
    """

# FreeCAD Layers for Tiles

alias / "tiles" / "LC(LA(K))"  # Launch FreeCAD Tiles
alias / "↑→" / macro("↑ →")
alias / "↑←" / macro("↑ ←")
alias / "↓→" / macro("↓ →")
alias / "↓←" / macro("↓ ←")

# Basically a number keypad and central tile shortcuts
layer / "fc0" / label("FC0") / r"""
    esc ,         7   8   9   *           ▽   ▽   ▽   ▽   ▽   ▽
    /   (fcv 0)   4   5   6   -           ▽   ▽   ▽   ▽   ▽   ▽
    tab .         1   2   3   +           ▽   ▽   ▽   ▽   ▽   ▽

    (fc0 /) (fcl ⌫) (fcr ⏎) (fc1 tiles)   ▽   ▽   ▽   ▽
    """

# Keys to move tiles slider
layer / "fc1" / label("FC1") / r"""
    ▽   ▽   ↑←   ↑    ↑→   ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   ←    ↓    →    ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   ↓←   p    ↓→   ▽           ▽   ▽   ▽   ▽   ▽   ▽
            ▽    ▽    ▽    ▽           ▽   ▽   ▽   ▽
    """

# Left tile shortcuts (Qwerty)
layer / "fcl" / label("FCL") / r"""
    ▽   ▽   q   w   e   ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   a   s   d   del         ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   z   x   c   ▽           ▽   ▽   ▽   ▽   ▽   ▽
            ▽   ▽   ▽   ▽           ▽   ▽   ▽   ▽
    """

# Right tile shortcuts (Qwerty)
layer / "fcr" / label("FCR") / r"""
    ▽   ▽   r   t   y   ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   f   g   h   del         ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   v   b   n   ▽           ▽   ▽   ▽   ▽   ▽   ▽
            ▽   ▽   ▽   ▽           ▽   ▽   ▽   ▽
    """

# Camera rotations
layer / "fcv" / label("FCV") / r"""
    ▽   ▽   u   i   o   ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   j   k   l   ▽           ▽   ▽   ▽   ▽   ▽   ▽
    ▽   ▽   ▽   ▽   ▽   ▽           ▽   ▽   ▽   ▽   ▽   ▽
            ▽   ▽   ▽   ▽           ▽   ▽   ▽   ▽
    """

# Some combos

combo(
    "zw",
    key_positions=[38, 41],
    layers=["def"],
)


# Generate files -------
from zkeymap.generators import zmk, qmk, svg, drawer

zmk.default_transform(layout, "marz44w", name="default_transform")
zmk.physical_layout(layout, "marz44w")
zmk.keymap(layout, "marz44w")

svg.layout(
    layout,
    "marz44w",
    options=svg.Options(outer=True),
)

svg.layout(
    layout,
    "marz44w_switches.svg",
    options=svg.Options(
        cap=False,
        switch=True,
        outer=False,
        cherry_pocket=True,
    ),
)

drawer.svg(layout, "marz44w")

qmk.info_json(layout, "marz44w")
