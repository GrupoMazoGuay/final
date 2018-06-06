init:
	pip install -r requirements.txt
	venv/bin/easy_install nose

test:
	venv/bin/python2.7 venv/bin/nosetests tests

coverage:
	coverage run code/textAnalizer.py
	coverage report -m