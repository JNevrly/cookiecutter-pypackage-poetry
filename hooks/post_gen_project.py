#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.rst")
        remove_file("docs/authors.rst")

    if "{{ cookiecutter.use_pytest }}" == "y":
        remove_file("tests/__init__.py")

    if "no" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if "{{ cookiecutter.use_pypi_deployment_with_travis }}" == "n":
        remove_file(".travis.yml")

    if "{{ cookiecutter.use_pypi_deployment_with_appveyor }}" == "n":
        remove_file("appveyor.yml")

    if "{{ cookiecutter.document_publisher }}" == "ReadTheDocs":
        remove_file("docs/.nojekyll")

    if "{{ cookiecutter.use_classic_aiohttp_setup }}" == "n":
        http_handler_file = os.path.join("{{ cookiecutter.project_slug }}",
                                         "http_handler.py")
        remove_file(http_handler_file)
