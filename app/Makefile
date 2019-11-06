.PHONY: run format test clean

test:
	source activate app && pytest -vv

lint:
	source activate app && black app/

update:
	conda env update

bootstrap:
	conda env create -f environment.yml

run:
	cd app ;\
	ln -s web cgi-bin ;\
	PYTHONPATH=/opt/anaconda3/envs/app/lib/python3.7/site-packages python -m http.server --cgi

clean:
	rm -rf app/cgi-bin
