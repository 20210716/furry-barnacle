python3 -m pip install --quiet pylint
pylint --ignore=dags --disable=C --disable=W1203 --disable=W1202 --reports=y --exit-zero "$@"
