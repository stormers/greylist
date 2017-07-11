.PHONY: clean run pep8 tests

PROJECT_HOME = "`pwd`"

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.~" -delete

run: clean
	@PYTHONPATH=`pwd`:$PYTHONPATH python api/run.py

pep8:
	@-pep8 $(PROJECT_HOME)

tests: clean pep8
	@py.test --cov-config .coveragerc --cov $(PROJECT_HOME) --cov-report term-missing
