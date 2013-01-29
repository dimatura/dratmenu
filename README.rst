========
dratmenu
========

A trivial python hack to select windows in Ratpoison with [dmenu](http://tools.suckless.org/dmenu/).

Usage
-----

Make sure you have a recent version of `dmenu` installed (it should have vertical
display capabilities).

You should have the `ratpoison.py` module somewhere it can be imported by the
main script. You can use the one that came with your ratpoison install (recommended)
or the one included in the repo. It should work either way.

Put the main script somewhere in your path and then bind it to a keystroke in
`.ratpoisonrc`, e.g. with `bind w exec dratmenu.py`. 

Use the numbers, keyboard arrows, or just type to select the window you want.

To customize colors, fonts and so on change the source code. It's just a few (hackish) lines.

Author
======

Daniel Maturana - dimatura@cmu.edu
