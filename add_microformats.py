#!/usr/bin/env python

"""
Render a Markdown template through Jinja
"""

import datetime
import io
import sys

from os.path import abspath, dirname, join as pjoin

from jinja2 import Environment, FileSystemLoader


SCHEMA_DIR = abspath(pjoin(dirname(__file__), 'schema'))
THIS_DIR = abspath(pjoin(dirname(__file__), ''))


def main(input_markdown, output_markdown):

    env = Environment(loader=FileSystemLoader([THIS_DIR, SCHEMA_DIR]))
    template = env.get_template(input_markdown)
    rendered_markdown = template.render(date_today=make_pretty_date())

    with io.open(output_markdown, 'w') as f:
        f.write(rendered_markdown)

    print("\nOutput written to {}".format(output_markdown))


def make_pretty_date(today=None):
    today = today or datetime.date.today()
    return today.strftime('%-d %B %Y')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <file.md> <output_file.md>".format(sys.argv[0]))
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2])
