# -*- coding: utf-8 -*-


from setuptools import setup


def readme():
    with open('README.md', 'r') as fp:
        return fp.read()


setup(
    name='slack_log_utils',
    version='0.1',
    description='A Python logging handler for Slack integration',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Logging'
    ],
    keywords='logging slack slack-webhook ngafid',
    url='https://github.com/ngafid/slack-log-utils',
    author='KeltonKarboviak',
    author_email='kelton.karboviak@gmail.com',
    license='MIT',
    packages=['slack_log_utils'],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    zip_safe=False,

    test_suite='nose.collector',
    tests_require=['nose'],
)
