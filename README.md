<!--
<p align="center">
  <img src="https://github.com/cthoyt/apicuron-client/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  APICURON Client
</h1>

<p align="center">
    <a href="https://github.com/cthoyt/apicuron-client/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/cthoyt/apicuron-client/workflows/Tests/badge.svg" />
    </a>
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-python--package-yellow" /> 
    </a>
    <a href="https://pypi.org/project/apicuron_client">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/apicuron_client" />
    </a>
    <a href="https://pypi.org/project/apicuron_client">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/apicuron_client" />
    </a>
    <a href="https://github.com/cthoyt/apicuron-client/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/apicuron-client" />
    </a>
    <a href='https://apicuron-client.readthedocs.io'>
        <img src='https://readthedocs.org/projects/apicuron_client/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://zenodo.org/badge/latestdoi/399071637">
        <img src="https://zenodo.org/badge/399071637.svg" alt="DOI">
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
</p>

An unofficial client for interacting with the [APICURON](https://apicuron.org/) curation
metadatabase.

## 💪 Getting Started

The following example shows how you can prepare a submission of a new resource
to APICURON. Because `apicuron_client` uses PyDantic under the hood, the JSON
is validated and automatically converted into programmatic models. The
`Description.update_remote()` function takes care of interacting with the API
and loading the `APICURON_TOKEN` from the environment or a config file with
[`pystow`](https://github.com/cthoyt/pystow).

```python
from apicuron_client import Description

payload = {
   "resource_id": "Biomappings",
   "resource_name": "Biomappings",
   "resource_uri": "https://biomappings.github.io/biomappings/",
   "resource_url": "https://biomappings.github.io/biomappings/",
   "resource_long_name": "Biomappings",
   "resource_description": "Community curated and predicted equivalences and related mappings between named biological entities that are not available from primary sources.",
   "terms_def": [
      {
         "activity_term": "novel_curation",
         "activity_name": "Curated novel mapping",
         "activity_category": "generation",
         "score": 50,
         "description": "Curated a novel mapping between two entities"
      },
      {
         "activity_term": "validate_prediction",
         "activity_name": "Validate predicted mapping",
         "activity_category": "generation",
         "score": 50,
         "description": "Affirmed the correctness of a predicted mapping"
      },
      {
         "activity_term": "invalidate_prediction",
         "activity_name": "Invalidate predicted mapping",
         "activity_category": "generation",
         "score": 50,
         "description": "Affirmed the incorrectness of a predicted mapping"
      }
   ],
   "achievements_def": [
      {
         "category": "1",
         "name": "Newbie curator",
         "count_threshold": 10,
         "type": "badge",
         "list_terms": [
            "novel_curation",
            "validate_prediction",
            "invalidate_prediction"
         ],
         "color_code": "#055701"
      }
   ]
}
description = Description(**payload)
description.update_remote()
```

The results can then be seen on the APICURON website at
https://apicuron.org/database?resource_uri=https:%2F%2Fbiomappings.github.io%2Fbiomappings%2F.

<!--
### Command Line Interface

The apicuron_client command line tool is automatically installed. It can
be used from the shell with the `--help` flag to show all subcommands:

```shell
$ apicuron_client --help
```

> TODO show the most useful thing the CLI does! The CLI will have documentation auto-generated
by `sphinx`.

-->

## 🚀 Installation

The most recent release can be installed from
[PyPI](https://pypi.org/project/apicuron_client/) with:

```bash
$ pip install apicuron_client
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/cthoyt/apicuron-client.git
```

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/cthoyt/apicuron-client.git
$ cd apicuron-client
$ pip install -e .
```

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.rst](https://github.com/cthoyt/apicuron-client/blob/master/CONTRIBUTING.rst) for more information on getting involved.

## 👀 Attribution

### ⚖️ License

The code in this package is licensed under the MIT License.

### 📖 Citation

This project isn't officially from the APICURON team, but if you like it, please cite their
paper:

```bibtex
@article{Hatos2021,
   author = {Hatos, Andr{\'{a}}s and Quaglia, Federica and Piovesan, Damiano and Tosatto, Silvio C E},
   doi = {10.1093/database/baab019},
   issn = {1758-0463},
   journal = {Database},
   month = {apr},
   title = {{APICURON: a database to credit and acknowledge the work of biocurators}},
   url = {https://academic.oup.com/database/article/doi/10.1093/database/baab019/6244733},
   volume = {2021},
   year = {2021}
}
```

## Acknowledgements

<!--
### 🎁 Support

This project has been supported by the following organizations (in alphabetical order):

- [Harvard Program in Therapeutic Science - Laboratory of Systems Pharmacology](https://hits.harvard.edu/the-program/laboratory-of-systems-pharmacology/)

-->

<!--
### 💰 Funding

This project has been supported by the following grants:

| Funding Body                                             | Program                                                                                                                       | Grant           |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------|
| DARPA                                                    | [Automating Scientific Knowledge Extraction (ASKE)](https://www.darpa.mil/program/automating-scientific-knowledge-extraction) | HR00111990009   |
-->

### 🍪 Cookiecutter

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) template.

## 🛠️ For Developers

The final section of the README is for if you want to get involved by making a code contribution.

### ❓ Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/cthoyt/apicuron-client/actions?query=workflow%3ATests).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses BumpVersion to switch the version number in the `setup.cfg` and
   `src/apicuron_client/version.py` to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel
3. Uploads to PyPI using `twine`. Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.
