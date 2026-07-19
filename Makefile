PYTHON ?= python3
NAME := Identity_Trust_Inclusion_Fabric_Thesis_v0.1.0

.PHONY: install experiment test paper verify clean package

install:
	$(PYTHON) -m pip install -e .[dev]

experiment:
	PYTHONPATH=src $(PYTHON) scripts/run_experiment.py

test:
	PYTHONPATH=src pytest -q

paper: experiment
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp paper/main.pdf output/pdf/$(NAME).pdf

verify: paper
	pdfinfo output/pdf/$(NAME).pdf
	mkdir -p tmp/pdfs/rendered
	pdftoppm -png -r 120 output/pdf/$(NAME).pdf tmp/pdfs/rendered/page >/dev/null 2>&1

package: paper test
	zip -r $(NAME)_FULL_SOURCE.zip README.md LICENSE CITATION.cff Makefile pyproject.toml config src scripts tests docs paper figures results output/pdf .github -x "*/__pycache__/*" "*.aux" "*.bbl" "*.bcf" "*.blg" "*.fdb_latexmk" "*.fls" "*.log" "*.out" "*.run.xml" "*.toc"

clean:
	cd paper && latexmk -C
	rm -rf tmp/pdfs/rendered

