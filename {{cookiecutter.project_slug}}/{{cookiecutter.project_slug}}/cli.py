# -*- coding: utf-8 -*-
"""
.. module: {{cookiecutter.project_slug}}.cli
   :synopsis: CLI interface
.. moduleauthor:: "{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"
"""

import sys
{%- if cookiecutter.use_onacol == 'y' %}
import pkg_resources
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- if cookiecutter.use_onacol == 'y' %}
from onacol import ConfigManager
{%- endif %}
{%- endif %}


{%- if cookiecutter.use_onacol == 'y' %}
DEFAULT_CONFIG_FILE = pkg_resources.resource_filename(
    "{{cookiecutter.project_slug}}", "default_config.yaml")
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
{%- if cookiecutter.use_onacol == 'y' %}
@click.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True
))
@click.option("--config", type=click.Path(exists=True), default=None,
              help="Path to the configuration file.")
@click.option("--get-config-template", type=click.File("w"), default=None,
              help="Write default configuration template to the file.")
@click.pass_context
def main(ctx, config, get_config_template):
    """Console script for {{cookiecutter.project_slug}}."""
    # Instantiate config_manager
    config_manager = ConfigManager(
        DEFAULT_CONFIG_FILE,
        env_var_prefix="{{cookiecutter.project_slug}}",
        optional_files=[config] if config else []
    )

    # Generate configuration for the --get-config-template option
    # Then finish the application
    if get_config_template:
        config_manager.generate_config_example(get_config_template)
        return

    # Load (implicit) environment variables
    config_manager.config_from_env_vars()

    # Parse all extra command line options
    config_manager.config_from_cli_args(ctx.args)

    # Validate the config
    config_manager.validate()

    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{% else %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""


    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- endif %}

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
