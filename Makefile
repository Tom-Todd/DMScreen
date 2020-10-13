PIPENV:=pipenv

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

check: flake8 pylint

isort-check:
	$(PIPENV) run isort -c -rc

flake8:
	$(PIPENV) run flake8

pylint:
	$(PIPENV) run pylint --rcfile=.pylintrc --output-format=colorized dmscreen
