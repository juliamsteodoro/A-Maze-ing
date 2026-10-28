.PHONY: install run debug clean lint lint-strict

install:
	python3 -m pip install flake8 mypy

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	@# TODO: Remover arquivos temporários e caches
	@echo "Cleaning temporary files..."
	rm -rf __pycache__ .mypy_cache .pytest_cache *.pyc

lint:
	flake8 .
	mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .

lint-strict:
	flake8 .
	mypy --strict .
