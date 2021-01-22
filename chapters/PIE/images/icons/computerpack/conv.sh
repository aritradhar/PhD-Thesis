#!/bin/bash
for svg in *.svg ; do
    inkscape -D -z --file=${svg} --export-pdf="${svg%.*}.pdf" --export-latex
done
