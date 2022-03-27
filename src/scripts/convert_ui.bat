@echo off

cd ..
cd gui\ui

for %%f in (*.ui) do (
  pyside6-uic %%~nf.ui -o %%~nf_ui.py
)