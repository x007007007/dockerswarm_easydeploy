# -*- coding: utf-8 -*-
from setuptools import setup

long_description = None
INSTALL_REQUIRES = [
    'django~=4.0',
    'docker~=5.0',
    'grpcio~=1.44.0',
    'requests',
    'djangorestframework',
    'django-filter',
    'markdown',
    'django_loguru',
    'django-autocomplete-light~=3.9.4',
]
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'isort',
    ],
    'builds': [
        'grpcio-tools',
    ],
}
ENTRY_POINTS = {
    'console_scripts': [
        'docker_swarm_easy_deploy_client = dockerswarm_easydeploy_client.__main__:main',
        'docker_swarm_easy_deploy_management = dockerswarm_easydeploy.__main__:main',
    ],
}

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
        'dockerswarm_easydeploy_client',
        'dockerswarm_easydeploy.apps',
        'dockerswarm_easydeploy.apps.core',
        'dockerswarm_easydeploy.apps.core.migrations',
        'dockerswarm_easydeploy.apps.core.admin',
        'dockerswarm_easydeploy.apps.core.models',
        'dockerswarm_easydeploy.apps.core.action',
        'dockerswarm_easydeploy.apps.core.api',
        'dockerswarm_easydeploy.apps.core.management.commands',
        'dockerswarm_easydeploy.apps.core.api.node',
    ],
    'package_dir': {'': 'src'},
    'package_data': {'': ['*']},
    'install_requires': INSTALL_REQUIRES,
    'extras_require': EXTRAS_REQUIRE,
    'python_requires': '>=3.10',
    'entry_points': ENTRY_POINTS,

}


setup(**setup_kwargs)

