#!/bin/bash
chmod u+x *.py
rm *-main.py
git add *.py
git commit -m "Add all"
git push origin main
