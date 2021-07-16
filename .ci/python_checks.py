from subprocess import CalledProcessError, check_call
from sys import argv, executable, exit, stderr

TARGET = "furry_barnacle"
CHECKS = {
    "black": {
        "packages": {
            "black",
        },
        "commands": [
            [
                "black",
                "--check",
                TARGET,
            ],
        ],
    },
    "mypy": {
        "packages": {
            "mypy",
            "types-python-dateutil",
            "types-PyYAML",
            "types-requests",
        },
        "commands": [
            f"mypy {TARGET} --ignore-missing-imports",
        ],
    },
    "pylint": {
        "packages": {
            "pylint",
        },
        "commands": [
            f"pylint {TARGET} --ignore=dags --disable=C --disable=W1203 --disable=W1202 --reports=y --exit-zero",
        ],
    },
    "complexity": {
        "packages": {
            "xenon",
        },
        "commands": [
            "xenon --max-absolute B --max-modules A --max-average A . -i transform,shared_modules",
        ],
    },
    "pytest": {
        "packages": {
            "pytest",
        },
        "commands": [
            "python -m pytest -vv -x --show-capture=no --junitxml=report.xml",
        ],
    },
}

if len(argv) > 1:
    checks_to_run = argv[1:]
else:
    checks_to_run = CHECKS.keys()

for name in checks_to_run:
    packages = CHECKS[name]["packages"]
    commands = [[executable, "-m", "pip", "install"] + list(packages)]
    commands += CHECKS[name]["commands"]
    for command in commands:
        shell = isinstance(command, str)
        if shell:
            commandstr = command
        else:
            commandstr = " ".join(command)
        print("+", commandstr, file=stderr)
        try:
            check_call(command, shell=shell)
        except CalledProcessError as cpe:
            exit(cpe.returncode)
