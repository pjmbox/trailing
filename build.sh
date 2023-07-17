#!/usr/bin/env bash

# conda activate pyqt6

rm -rf dist
#pyinstaller -F -w -i wind.ico setup.py
pyinstaller -F -w -n trailing -i resources/trailing.png main.py
cp cf_actions.yaml  cf_aliases.yaml  cf_config.yaml  cf_highlight.yaml dist/
cp -a resources dist/
rm -f trailing.spec
rm -rf build

# conda deactivate
