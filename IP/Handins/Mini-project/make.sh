#!/bin/bash
latexmk -pdf -output-directory=auxdir
mv auxdir/*.pdf .
