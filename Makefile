init:
	pip install -r requirements.txt
	bin/easy_install nose

test:
	nosetests tests

# coverage:
# 	coverage run code/xxxxxx.py
# 	coverage report -m

run:
	python code/application.py