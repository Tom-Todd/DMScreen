PIPENV:=pipenv
# ===============
# Static analysis
# ===============

check: flake8 pylint

isort-check:
	$(PIPENV) run isort -c -rc

flake8:
	$(PIPENV) run flake8

pylint:
	$(PIPENV) run pylint --rcfile=.pylintrc --output-format=colorized dmscreen
