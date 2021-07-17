poetry run pylint --ignore=dags --disable=C --disable=W1203 --disable=W1202 --reports=y --exit-zero "$@"
