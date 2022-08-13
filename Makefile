SRC_DIR = src/hrm
TEST_DIR = tests

PY_ENV = venv
PY_BIN = $(PY_ENV)/bin

all: $(PY_BIN)/hrm


$(PY_BIN)/python:
	python -m venv $(PY_ENV)
	chmod +x $(PY_BIN)/activate
	./$(PY_BIN)/activate


$(PY_BIN)/pip3: $(PY_BIN)/python


$(PY_BIN)/hrm: $(PY_BIN)/pip3
	$(PY_BIN)/pip3 install -e .


$(PY_BIN)/pytest: $(PY_BIN)/pip3
	$(PY_BIN)/pip3 install -r $(TEST_DIR)/requirements.txt


tests: $(PY_BIN)/pytest $(PY_BIN)/hrm
	$(PY_BIN)/pytest $(TEST_DIR)/*.py


clean:
	rm -rf */__pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache


fclean: clean
	rm -rf $(PY_ENV)
	rm -rf build


.PHONY: py_test clean fclean tests
