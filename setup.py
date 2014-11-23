from setuptools import setup

setup(
    name = 'OpenAddresses',
    version = '0.1.0',
    packages = ['openaddr'],
    package_data = {
        'openaddr': [
            'geodata/*.shp', 'geodata/*.shx', 'geodata/*.prj', 'geodata/*.dbf',
            'geodata/*.cpg', 'templates/*.html'
        ]
    },
    install_requires = [
        'boto >= 2.0.0', 'Jinja2 >= 2.7.0', 'dateutils >= 0.6',
        
        # https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991/comments/10
        'requests==2.2.1'
        ],
    entry_points = dict(
        console_scripts = [
            'openaddr-render-us = openaddr.render:main',
            'openaddr-summarize = openaddr.summarize:main',
            'openaddr-process = openaddr.process:main'
        ]
    )
)