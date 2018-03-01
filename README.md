# How IF uses data

This is the source code to the policy at [www.projectsbyif.com/how-if-uses-data](https://www.projectsbyif.com/how-if-uses-data).

We use [schema.org](https://schema.org) microformats to describe the third party services we use in a machine-readable way.

In the markdown file we use `{% include "service_name.html" %}` to include a file from the [`schema/`](https://github.com/projectsbyif/how-if-uses-data/blob/master/schema/) subdirectory.

## How to update

- On your own machine, edit the file `markdown/how-if-uses-data.md`
- Run `make` to regenerate `output/how-if-uses-data.md`
- Copy & paste from `output/how-if-uses-data.md` into our CMS
