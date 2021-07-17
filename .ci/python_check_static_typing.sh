python3 -m pip install --quiet mypy types-python-dateutil types-PyYAML types-requests
mypy --ignore-missing-imports "$@"
