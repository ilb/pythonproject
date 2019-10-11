.PHONY: bootstrap clean lint test

test:
	conda activate library && python -m unittest discover
	# or another way

lint:
	# add some lint here

update:
	conda env update

bootstrap:
	conda env create -f environment.yml

run dev:
	cd app; \
	source activate app && python -m http.server --cgi
