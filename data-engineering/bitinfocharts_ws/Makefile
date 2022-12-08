.PHONY: clean
## clean : clean project files
clean:
	rm -rf build/ dist/ *.egg-info .eggs .coverage htmlcov .mypy_cache
	find . -name '*pycache' -exec rm -rf {} +

.PHONY: deps
## deps: install dependencies
deps:
	pip install -r requirements.txt

.PHONY: check
## check: Use mypy to lint source codes
check:
	mypy main.py

.PHONY: run
## run: Run main.py
run:
	python3 main.py
	
.PHONY: help
all:help
#help: show this  help message
help: Makefile
	@echo
	@echo " Choose a command to run in "$(NAME)":"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' | sed -e 's/^/ /'
	@echo