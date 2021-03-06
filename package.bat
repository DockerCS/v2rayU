@echo off
echo update...
pip install -U setuptools wheel twine
echo package...
python setup.py sdist bdist_wheel
echo upload...
twine upload dist/*
echo clean..
if exist dist (
    rd /s /Q build
    rd /s /Q dist
    rd /s /Q v2rayU.egg-info
    rd /s /Q v2rayU\__pycache__
    rd /s /Q v2rayU\util_core\__pycache__
)
echo finish!
pause