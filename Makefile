SRC_DIR = src/hrm

PY_ENV = venv
PY_BIN = $(PY_ENV)/bin


all: $(PY_BIN)/hrm


$(PY_BIN)/hrm: $(PY_BIN)/pip3
	$(PY_BIN)/pip3 install -e .


$(PY_BIN)/pip3: $(PY_BIN)/python

$(PY_BIN)/python:
	python -m venv $@
	chmod +x $@/bin/activate
	./$@/bin/activate


clean:
	@ rm -rf .pytest_cache
	@ rm -rf .mypy_cache


fclean: clean
	@ rm -rf $(PY_ENV)


.PHONY: py_test clean fclean
