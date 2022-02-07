
# -*- coding: utf-8 -*-
from setuptools import setup

long_description = None
INSTALL_REQUIRES = [
    'django~=4.0',
    'docker~=5.0',
]

setup_kwargs = {
    'name': 'docker_swarm_easy_deploy',
    'version': '0.1.0',
    'description': '',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'xingci.xu <x007007007@hotmail.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'dockerswarm_easydeploy',
        'dockerswarm_easydeploy.apps',
        'dockerswarm_easydeploy.apps.core',
        'dockerswarm_easydeploy.apps.core.migrations',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.10',

}


setup(**setup_kwargs)

