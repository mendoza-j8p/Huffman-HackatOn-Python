SHELL:=/bin/bash

direnv=$(PWD)/venv-nuwe/

.PHONY: test 

$(direnv):
	echo "Setting up virtual environment";
	python3 -m venv $(direnv)
	echo "Correctly setup virtual environment in $(direnv)";
	source $(direnv)bin/activate && \
	pip install -r requirements.txt 

test: | $(direnv)
	source $(direnv)bin/activate && \
	$(direnv)bin/python3 -m pytest $(ARGS)

run: | $(direnv)
	source $(direnv)bin/activate && \
	$(direnv)bin/python3 main.py


