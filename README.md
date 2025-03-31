# Marz44W Split BLE Dongle Keyboard

Yet another Split Keyboard.

![picture](pic1.jpeg)

## Features

- Wireless Split
- USB Dongle
- ZKeymap based
- Up to 4 Bluetooth devices plus the main USB host

## Layout

```python
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

            ▽   ▽   ▽   ▽         ▽   ▽   ▽   ▽
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

```

## Layout graphics

![Layout](config/boards/shields/marz44w/marz44w_layout.svg)

## ZKeymap

To generate dtsi, keymap, json and svg files, install zkeymap and execute keymap.py

```bash
pip install zkeymap
cd config/boards/shields/marz44w
python keymap.py
```

Ref: [https://github.com/mnesarco/zkeymap](https://github.com/mnesarco/zkeymap)