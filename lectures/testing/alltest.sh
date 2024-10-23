#!/usr/bin/env bash

PRG="dna.py"

for FILE in dna[0-9].py; do
    echo "Testing \"$FILE\""
    cp "$FILE" "$PRG"
    ARGS="tests/dna_test.py"
    [[ $FILE != "dna1.py" ]] && ARGS="${ARGS} dna.py"
    pytest -xv $ARGS
done

echo "Done."
