# fmt: off

# Import zkeymap language artifacts
from zkeymap import (
    alias,
    layer,
    label,
    build_keymap,
    build_transform,
    build_layout_json,
    build_layout_svg,
    layout,
    keys,   # Import base key definitions
    keys_la # Import Language specific keys (Latam)
)


# Import or define a physical layout
from zkeymap.layouts import marz_split_3x6_4
layout /= marz_split_3x6_4.layout


# Select Linux unicode composers
uc = keys.UnicodeLinux

# User defined aliases
alias / "cw" /  "&caps_word"
alias / "zw"/ "LC(LA(DOWN))" # Windows Zoom (Linux Mint)
alias / "∴" / uc("∴", "∴", name="t3p")

# Layers -----------------

layer / "def" / label("DEF") / r"""
    {⌘ esc} [ q ] [ w ] [ f ] [ p ] [ b ]      [ j ] [ l ] [ u ] [ y ] [ acut ]    [ñ]
    {⎇ tab} {⇧ a} [ r ] [ s ] [ t ] [ g ]      [ m ] [ n ] [ e ] [ i ] {⇧ o}      <cw>
    {⎈  \ } [ z ] [ x ] [ c ] [ d ] [ v ]      [ k ] [ h ] [ , ] [ . ] [ ; ]     [ ⏎ ]
          (num tab) (sym ⌫) (nav ␣) [⇧ ⎇]      [r⎇] (nav ␣) (sym ⌫) (adj del)
    """

layer / "num" / label("NUM") / r"""
    _____   [ * ] [ 7 ] [ 8 ] [ 9 ] [ / ]      [ / ] [ 7 ] [ 8 ] [ 9 ] [ * ] [ ∴ ]
    [ , ]   [ 0 ] [ 4 ] [ 5 ] [ 6 ] [ - ]      [ - ] [ 4 ] [ 5 ] [ 6 ] [ 0 ] [ , ]
    [ zw ]  [ . ] [ 1 ] [ 2 ] [ 3 ] [ + ]      [ + ] [ 1 ] [ 2 ] [ 3 ] [ . ] _____
                  _____ _____ _____ _____      _____ _____ _____ _____
    """

layer / "sym" / label("SYM1") / r"""
    [ | ]    [ ! ] [ " ] [ # ] [ $ ] [ % ]      [ & ] [ / ] [ [ ] [ \] ] [ = ] [ ? ]
    [ grv ]  [ * ] [ ' ] [ : ] [ _ ] [ - ]      [ - ] [ ( ] [ ) ] [ {  ] [ } ] _____
    [ diae ] [ @ ] [ ~ ] [ ^ ] [ = ] [ + ]      [ + ] [ ' ] [ < ] [ >  ] [ \ ] _____
                   (adj) _____ _____ _____      _____ _____ (num~) _____
    """

layer / "nav" / label("NAV") / r"""
    _____ [ f1 ] [ f2 ] [ f3 ] [ f4 ] [ f5  ]     _____     [ pgup ] [  ↑  ] [ pgdn ] [  f10 ] [ f11 ]
    _____ [ ⇧  ] [ '  ] [ :  ] [ _  ] [ -   ]     [  home ] [   ←  ] [  ↓  ] [   →  ] [  end ] [ f12 ]
    _____ [ f6 ] [ f7 ] [ f8 ] [ f9 ] [ f10 ]     [ ⎈ home] [ ⎈ ←  ]  xxxxx  [ ⎈ →  ] [⎈ end ]  _____
                      _____ _____ _____ _____     _____ _____ _____ _____
    """

layer / "adj" / label("ADJ") / r"""
    <⚙>    _____     _____   _____ _____ _____      _____ _____ _____ _____ _____ <⚙>
    <ᛒclr> <ᛒ0>      <ᛒ1>    <ᛒ2>  <ᛒ3>  <ᛒ4>       <ᛒ4>  <ᛒ3>  <ᛒ2>  <ᛒ1>  <ᛒ0>  <ᛒclr>
    _____  [ nlck ]  <usb/ᛒ> _____ _____ _____      _____ _____ _____ _____ _____ _____
                     _____   _____ _____ _____      _____ _____ _____ _____
    """

# Generate files -------

build_keymap("marz44w_inc.keymap")
build_transform("marz44w_transform_inc.dtsi")
build_layout_json("marz44w_layout.json")
build_layout_svg("marz44w_layout.svg")
