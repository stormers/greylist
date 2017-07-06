.PHONY: clean run

PROJECT_HOME = "`pwd`"

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.~" -delete

run: clean
	@PYTHONPATH=`pwd`:$PYTHONPATH python api/run.py
