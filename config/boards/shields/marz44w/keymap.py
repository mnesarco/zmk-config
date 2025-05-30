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

# Import generators
from zkeymap.generators import zmk, qmk, svg

# Select physical layout
layout = marz_split_3x6_4.layout

# User defined aliases
alias / "cw" / "&caps_word" / label("⇪")
alias / "zw" / "LC(LA(DOWN))"  # Windows Zoom out (Linux Mint)
alias / ("sel*", "⬚") / "LC(A)"  # Select All
alias / "∴" / uc(name="t3p", char="∴", shifted="△")  # Fancy unicode chars

# Layers -----------------

thumbs = "▽ ▽ ▽ ▽  ▽ ▽ ▽ ▽"

# Base layer: Colemak-DH (Spanish, Latam, Dead keys)
layer / "def" / label("DEF") / (
    r"""
    {⌘ esc}    q     w   f   p   b          j   l   u   y   acut     ñ
    {⎇ tab}  {⇧ a}   r   s   t   g          m   n   e   i   {⇧ o}   cw
    {⎈  \ }    z     x   c   d   v          k   h   ,   .     ;      ⏎
    """
    # Thumbs ...
    r"""
    (num tab)  (sym ⌫)  (nav ␣)  [⇧ ⎇]     [r⎇]  (nav ␣)  (sym ⌫)  (adj del)
    """
)

# Numeric layer: Left and Right handed numeric keypad
layer / "num" / label("NUM") / (
    r"""
    ▽   ,   7   8   9   -         -   7   8   9   ,   ∴
    /   *   4   5   6   0         0   4   5   6   *   /
    tab .   1   2   3   +         +   1   2   3   .   ▽

          ▽ (fc0 /) ▽   ▽         ▽   ▽   ▽   ▽
    """
)

# Symbols layer: General symbols layer (custom layout for coding)
layer / "sym" / label("SYM1") / (
    r"""
    |      !   "  [#]  $   %       &     /    [ [ ]  [ \] ]    =     ?
    grv    *   '   :   _   -       -   [ ( ]  [ ) ]  [ {  ]  [ } ]   ▽
    diae   @   ~   ^   =   +       +     '    [ < ]  [ >  ]  [ \ ]   ▽

            (adj)  ▽   ▽   ▽       ▽  ▽  (num ~) ▽
    """
)

# Navigation layer: WIP
layer / "nav" / label("NAV") / (
    r"""
    ▽  f1  f2  f3  f4  f5       ▽         [ pgup ]  [  ↑  ]  [ pgdn ]  [  f10 ]  [ f11 ]
    ▽  ⇧   '   :   _   -        [ home ]  [   ←  ]  [  ↓  ]  [   →  ]  [  end ]  [ f12 ]
    ▽  f6  f7  f8  f9  f10      [⎈ home]  [ ⎈ ←  ]   xxxxx   [ ⎈ →  ]  [⎈ end ]     ▽
    """,
    thumbs,
)

# Configuration later: Bluetooth, usb and flashing setup
layer / "adj" / label("ADJ") / (
    r"""
    ⚙      ▽     ▽     ▽   ▽   ▽      ▽   ▽   ▽   ▽   ▽   ⚙
    ᛒclr   ᛒ0    ᛒ1    ᛒ2  ᛒ3  ᛒ4     ᛒ4  ᛒ3  ᛒ2  ᛒ1  ᛒ0  ᛒclr
    ▽      nlck  usb/ᛒ ▽   ▽   ▽      ▽   ▽   ▽   ▽   ▽   ▽
    """,
    thumbs,
)

# ┌─────────────────────────────────────────────────────┐
# │ FreeCAD Tiles Keypad                                │
# └─────────────────────────────────────────────────────┘
#   Layers for Tiles and general FreeCAD usage
#   Left hand only (right hand is for pointing device)


mod = "⎈ ⌘" # Combined Mod: Ctrl+GUI
alias / "tiles" / "LC(LA(K))" / label("▯▮▯")  # Launch FreeCAD Tiles
alias / "|↖|" / macro(f"[{mod} ⎇ ↑]") / label("↖")
alias / "|↗|" / macro(f"[{mod} ⎇ ↓]") / label("↗")
alias / "|↙|" / macro(f"[{mod} ⎇ ←]") / label("↙")
alias / "|↘|" / macro(f"[{mod} ⎇ →]") / label("↘")
alias / "|↑|" / macro(f"[{mod} ↑]") / label("↑")
alias / "|↓|" / macro(f"[{mod} ↓]") / label("↓")
alias / "|←|" / macro(f"[{mod} ←]") / label("←")
alias / "|→|" / macro(f"[{mod} →]") / label("→")
alias / "|w|" / macro(f"[{mod} w]") / label("⛁")
alias / "|C|" / "LC(LG(C))" / label("☉") # Camera eye
alias / "↥" / macro(f"[{mod} ⇧ ↑]")
alias / "↧" / macro(f"[{mod} ⇧ ↓]")
alias / "VF" / macro("v f")
alias / ("UNDO", "↶") / "LC(Z)"
alias / ("REDO", "↷") / "LS(LC(Z))"

# Base FreeCAD layer: Left-handed numeric pad
#   with access to FreeCAD related layers at thumbs.
# Tiles slider layer: Central column shortcuts.
layer / "fc0" / label("FC0") / (
    r"""
    esc  ,      7      8      9      -        ▽ ▽ ▽ ▽ ▽ ▽
    /    {⌘ 0}  {⎇ 4}  {⇧ 5}  {⎈ 6}  *        ▽ ▽ ▽ ▽ ▽ ▽
    tab  .      1      2      3      +        ▽ ▽ ▽ ▽ ▽ ▽

    (fc0 /)  (fcl ⌫)  (fcr ⏎)  (fc1 tiles)
    ▽ ▽ ▽ ▽
    """
)

# Tiles Slider layer: Keys to move tiles slider and select worlds.
# Camera Controller layer: Rotation/Pan/Zoom/Center.
layer / "fc1" / label("FC1") / (
    r"""
    [⎈ ⇧ f5]  [⎈ ⇧ f6]   |↖|  |↑|  |↗|   ↥      ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ ⇧ f3]  [⎈ ⇧ f4]   |←|  |↓|  |→|   ↧      ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ ⇧ f1]  [⎈ ⇧ f2]   |↙|  |w|  |C|   VF     ▽ ▽ ▽ ▽ ▽ ▽

    ▽ ▽ ▽ ⌽
    ▽ ▽ ▽ ▽
    """,
)

# Parenthesis layer: Keys to type all kind of parenthesis
# Tiles slider layer: Left column shortcuts
layer / "fcl" / label("FCL") / (
    r"""
    [⎈ ⇧ f11]  [⎈ ⇧ f12]   [ > ]  [ { ]  [ }  ]  UNDO      ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ ⇧ f9 ]  [⎈ ⇧ f10]   [ < ]  [ ( ]  [ )  ]  REDO      ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ ⇧ f7 ]  [⎈ ⇧ f8 ]   [ _ ]  [ [ ]  [ \] ]  =         ▽ ▽ ▽ ▽ ▽ ▽

    ▽ ⌽ ▽ ▽
    ▽ ▽ ▽ ▽
    """,
)

# Tiles slider layer: Right column shortcuts
# Sketcher layer: Frequent Constraints
layer / "fcr" / label("FCR") / (
    r"""
    [⎈ f5]  [⎈ f6]   p  c  n  sel*    ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ f3]  [⎈ f4]   s  d  e  del     ▽ ▽ ▽ ▽ ▽ ▽
    [⎈ f1]  [⎈ f2]   a  m  t  =       ▽ ▽ ▽ ▽ ▽ ▽

    ▽ ▽ ⌽ ▽
    ▽ ▽ ▽ ▽
    """,
)


# Some combos (for testing....)
combo(
    "zw",
    key_positions=[38, 41],
    layers=["def"],
)


# Generate files -------

zmk.default_transform(layout, "marz44w", name="default_transform")
zmk.physical_layout(layout, "marz44w")
zmk.keymap(layout, "marz44w")

svg.layout(
    layout,
    "marz44w",
    options=svg.Options(outer=True),
    layers=["fc0", "fc1", "fcl", "fcr"],
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
    layers=["fc0", "fc1", "fcl", "fcr"],
)

qmk.info_json(layout, "marz44w")
