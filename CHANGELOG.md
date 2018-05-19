# Release Notes

## 0.1.5 (2018-05-19)
* Modified .travis.yml
    * Added skip_existing flag to deployments. This will stop parallel builds from failing (see [here](https://stackoverflow.com/questions/46387129/preventing-conflicts-when-deploying-multiple-distros-to-pypi-using-travis-ci)).
    * Made it so all branches will be built, but keeping that only tagged commits on master branch will be deployed to PyPI.
* Updated README with badges from shields.io.

## 0.1.4 (2018-05-19)
* Modified .travis.yml to fix issue with Travis-CI skipping deployment although the commit was tagged (see [here](https://stackoverflow.com/questions/30156581/travis-ci-skipping-deployment-although-commit-is-tagged#31282158)).

## 0.1.3 (2018-05-19)
* Small code style change in slack_webhook_formatter.py.

## 0.1.2 (2018-05-19)
* Added .travis.yml file for Travis-CI builds.

## 0.1.1 (2018-05-19)
* Bumped version for README changes to show on PyPI.

## 0.1.0 (2018-05-19)
* First release on PyPI.
