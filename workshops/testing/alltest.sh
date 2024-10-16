#!/usr/bin/env bash

PRG="dna.py"

for FILE in dna[0-9].py; do
    echo "Testing \"$FILE\""
    cp "$FILE" "$PRG"
    pytest -xv
    [[ $? -ne 0 ]] && exit
done

echo "Done."
