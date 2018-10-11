# -*- coding: utf-8 -*-

letterBindings = (
    ("a", r"\alpha"),
    ("A", r"\Alpha"),
    ("b", r"\beta"),
    ("B", r"\Beta"),
    ("g", r"\gamma"),
    ("G", r"\Gamma"),
    ("d", r"\delta"),
    ("D", r"\Delta"),
    ("e", r"\varepsilon"),
    ("E", r"\Epsilon"),
    ("z", r"\zeta"),
    ("Z", r"\Zeta"),
    # eta?
    # theta?
    # iota?
    ("k", r"\kappa"),
    ("K", r"\Kappa"),
    ("l", r"\lambda"),
    ("L", r"\Lambda"),
    ("m", r"\mu"),
    ("M", r"\Mu"),
    ("n", r"\nu"),
    ("N", r"\Nu"),
    ("x", r"\xi"),
    ("X", r"\xi"),
    # omikron?
    ("p", r"\pi"),
    ("P", r"\Pi"),
    ("r", r"\rho"),
    ("R", r"\Rho"),
    ("s", r"\sigma"),
    ("S", r"\Sigma"),
    ("t", r"\tau"),
    ("T", r"\Tau"),
    ("u", r"\upsilon"),
    ("U", r"\Upsilon"),
    ("f", r"\varphi"),
    ("F", r"\Phi"),
    ("c", r"\chi"),
    ("C", r"\Chi"),
    # psi?
    ("o", r"\omega"),
    ("O", r"\Omega"),

    ("+`;", r"\colon"),
    ("+8", "NumpadMult", r"\cdot"),
    ("/", r"\frac{"),
    ("+`", r"\widetilde{"),

    ("[", r"\left["),
    ("]", r"\right]"),
    ("+9", r"\left("),
    ("+0", r"\right)"),
)

sequenceBindings = (
    ("=>", r"\Rightarrow"),
    ("->", r"\rightarrow"),
    ("<-", r"\leftarrow"),
    ("<--", r"\longleftarrow"),

    ("00", r"\infty"),

    ("<=", r"\leqslant"),
    (">=", r"\geqslant"),

    ("||", r"\left|\right|"),

    ("\l", r"\limits"),
)


def checkLetterBindings():
    letters = set()

    for letterBinding in letterBindings:
        for letter in letterBinding[:-1]:
            assert letter not in letters, "Second binding for %s" % letter

            letters.add(letter)


checkLetterBindings()
