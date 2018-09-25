# -*- coding: utf-8 -*-

import os

from string_constants import FILE_BEGIN, FILE_END, LETTER_BINDING, SEQUENCE_BINDING
from bindings import letterBindings, sequenceBindings


OUTPUT_FILE_PATH = "output/ahk4latex.ahk"

if "/" in OUTPUT_FILE_PATH:
    outputDir = OUTPUT_FILE_PATH[:OUTPUT_FILE_PATH.rfind("/")]

    os.makedirs(outputDir, exist_ok=True)


outputFile = open(file=OUTPUT_FILE_PATH, mode="w", encoding="utf-8")


print(FILE_BEGIN, file=outputFile)

for letterBinding in letterBindings:
    sources = letterBinding[:-1]
    to = letterBinding[-1]

    for source in sources:
        if source.isupper():
            sourceAhk = "+" + source.lower()
        else:
            sourceAhk = source

        print(LETTER_BINDING.format(source=source, sourceAhk=sourceAhk, to=to), file=outputFile)

for sequenceBinding in sequenceBindings:
    sources = sequenceBinding[:-1]
    to = sequenceBinding[-1]

    for source in sources:
        print(SEQUENCE_BINDING.format(source=source, sourceAhk=source, to=to), file=outputFile)

print(FILE_END, file=outputFile)
