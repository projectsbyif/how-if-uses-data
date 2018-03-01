SCHEMA_FILES := $(shell find schema -name '*.html')

output/how-if-uses-data.md: markdown/how-if-uses-data.md $(SCHEMA_FILES) add_microformats.py venv
	@mkdir -p output
	. venv/bin/activate; \
	python add_microformats.py $< $@

.PHONY: clean
clean:
	rm -rf output


venv:	requirements.txt
	virtualenv venv
	. venv/bin/activate; \
	pip install -r requirements.txt
