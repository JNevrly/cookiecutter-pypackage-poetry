# -*- coding: utf-8 -*-
"""
.. module: {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}
   :synopsis: Main module
.. moduleauthor:: "{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"
"""


{% if cookiecutter.use_classic_aiohttp_setup == 'y' %}
import asyncio
import logging
from .http_handler import HttpHandler


logger = logging.getLogger("{{cookiecutter.project_slug}}")


class {{cookiecutter.project_slug}}:

    def __init__(self, config, loop=None):
        self._config = config
        self._loop = loop or asyncio.get_event_loop()

        # UI
        self._http_handler = HttpHandler(
            self,
            log_level=getattr(logging, self._config["general"]["log_level"]))
        self._http_task = None



    def start(self):
        # UI
        self._http_task = self._loop.create_task(self._http_handler.run(
            host=self._config['ui']['addr'],
            port=self._config['ui']['port']
        ))

    def stop(self):
        # UI
        self._http_handler.shutdown()

{%- endif %}
