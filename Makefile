# Usage:
# make clean  # remove ALL binaries and objects
# make check
# make cov
# make watch-check


VENV = pipenv run

PYTEST = $(VENV) python -m pytest --tb=short tests/ --report-log=.pytest_cache/pytest.json

.PHONY: all
all:
	@echo "No action taken"

.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .coverage
	rm -fr .pytest_cache

.PHONY: check
check:
	$(PYTEST)

.PHONY: coverage
coverage:
	$(PYTEST) --cov-report term-missing --cov=whathappened/

.PHONY: watch-check
watch-check:
	$(VENV) ptw --runner="$(PYTEST)" \
		--onpass "notify-send -i emblem-default Pytest \"All Tests Pass!\"" \
		--onfail "python3 tests/misc/pytest-summary.py .pytest_cache/pytest.json \
		| xargs -r -i notify-send -i error Pytest \"{}\""

.PHONY: install
install:
	mkdir -p .venv
	pipenv sync

.PHONY: uninstall
uninstall: ## remove virtual environment
	pipenv --rm

test-release: dist ## package and upload a release to the test PyPI
	python3 -m twine upload -r pypitest dist/*

release: dist ## package and upload a release
	python3 -m twine upload dist/*

dist: clean ## builds source and wheel package
	python3 setup.py sdist bdist_wheel
	ls -l dist
