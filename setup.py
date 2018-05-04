from setuptools import setup

setup(
    name='render_comments',
    version='0.1',
    packages=['render_comments'],
    package_data = {'render_comments': ['templates/*html'],},
    url='https://github.com/PFTL/website_comments',
    license='MIT',
    author='Aquiles Carattino',
    author_email='aquiles@uetke.com',
    description='',
    test_suite='testsuite.testsuite',
    entry_points={
        'console_scripts':[
            'render_comments = render_comments.render_comments:main'
        ],
    },
    install_requires=[
        'PyYAML',
        'Jinja2',
        'markdown',
    ],
)