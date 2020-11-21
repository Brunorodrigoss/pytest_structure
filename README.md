# pytest_structure

This repository contains example code for *An Introduction to pytest*,
a [Test Automation University](https://testautomationu.applitools.com/) course
taught by [Andrew "Pandy" Knight](https://twitter.com/AutomationPanda).
This course teaches how to automate test cases in Python using [pytest](https://pytest.org).


## Repository Purpose

The best way to learn pytest is through hands-on coding.

## Repository Branches

* `master` contains the README but no example code
* Each `example/*` branch contains chapter-specific example code
* `example/develop` contains the completed example code for the end of the course


## Python Setup

Python setup can be complicated.
This section documents how to set up your machine for Python test automation development.

### Python Installation and Tools

This project requires Python 3.
You can download the latest Python version from [Python.org](https://www.python.org/downloads/).
Follow the appropriate installation instructions for your operating system.

Learning the language is always a prerequisite for learning automation.
If you need help learning Python, check out this article:
[How Do I Start Learning Python?](https://automationpanda.com/2020/02/18/how-do-i-start-learning-python/)

You should also have a good Python editor/IDE.
Good choices include [PyCharm](https://www.jetbrains.com/pycharm/)
and [Visual Studio Code](https://code.visualstudio.com/docs/languages/python).

You will also need [Git](https://git-scm.com/) if you want to clone this repository locally.
If you are new to Git, [try learning the basics](https://try.github.io/).

### Python Installation Troubleshooting

Unfortunately, installing Python properly can be complicated,
especially if Python was previously installed on your machine.
To verify your Python installation, enter `python --version` at the command line.
You should see the proper version printed.

If the `python` command doesn't work or doesn’t print the expected version number,
then try using the `python3` command instead.
If that still doesn't work,
then the correct Python installation might not be included in your system path.
Find the directory into which Python was installed,
manually add it to the system path,
relaunch the command line,
and try running Python again.

* [System Path Instructions for Windows](https://geek-university.com/python/add-python-to-the-windows-path/)
* [System Path Instructions for macOS](https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac)
* [System Path Instructions for Linux](https://www.computerhope.com/issues/ch001647.htm)

### Python Packages

This project will use a handful of third-party packages:

* pytest
* pytest-cov
* pytest-html
* pytest-xdist
* requests

These packages are *not* part of Python's standard library.
They must be installed separately using `pip`, the standard Python package installer.
You can install them all before you create your test project.

To install each package, enter `pip install <package-name>` at the command line.
For example: `pip install pytest`.
If you already have a package installed but need to upgrade its version,
run `pip install --upgrade <package-name>`.

Please note that if you need to use the `python3` command to run Python,
then you might also need to use the `pip3` command in lieu of `pip`.

### Virtual Environments

Running `pip install` will install the pytest package globally for the whole system.
Installing Python packages globally is okay for this project,
but it typically isn't a best practice in the "read world."
Instead, each project should manage its own dependencies locally using a virtual environment.
Virtual environments let projects avoid unnecessary dependencies and version mismatches.

If you would like to learn virtual environments on your own, then RealPython's article
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
is an excellent place to start.

###  Versions

This project was developed and tested using the following versions:

* macOS 10.14.6
* Python 3.8.1
* pytest 5.4.3
* pytest-cov 2.10.0
* pytest-html 2.1.1
* pytest-xdist 1.32.0
* requests 2.23.0


## Running Tests

To run the example tests from the command line, run `python -m pytest` from the project root directory.
This command will discover and run all tests in the project.

You can also run tests using the shorter `pytest` command.
However, I recommend always using the lengthier `python -m pytest` command.
The lengthier command automatically adds the current directory to `sys.path`
so that all modules in the project can be discovered.

The pytest command has several command line options.
Course material will cover many of them.
Check out the [Usage and Invocations](https://docs.pytest.org/en/stable/usage.html) page
for complete documentation.

*Warning:*
If you attempt to run tests from this example project,
make sure to checkout the correct branch first!


## Additional Resources

Python links:

* [Python.org](https://www.python.org/)
* [pytest.org](https://docs.pytest.org/)
* [How Do I Start Learning Python?](https://automationpanda.com/2020/02/18/how-do-i-start-learning-python/)
* [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
* [Effective Python Testing with Pytest](https://realpython.com/pytest-python-testing/)
* [Automation Panda's Python Page](https://automationpanda.com/python/)

Books:

* [Python Testing with pytest](https://pragprog.com/titles/bopytest/) by Brian Okken
* [pytest Quick Start Guide](https://www.packtpub.com/web-development/pytest-quick-start-guide) by Bruno Oliveira
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) by Harry J.W. Percival

Related TAU courses:

* [Python Programming](https://testautomationu.applitools.com/python-tutorial/)
* [Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
* [Behavior-Driven Python with pytest-bdd](https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/)
* [Automated Visual Testing with Python](https://testautomationu.applitools.com/visual-testing-python/)

Resources:
* [pytest documentation](https://pytest.org/)
* [GitHub repository for the pytest project](https://github.com/pytest-dev/pytest)
* [Python virtual environments](https://realpython.com/python-virtual-environments-a-primer/)
* [Python venv module](https://docs.python.org/3/library/venv.html)
* [pytest discovery](https://docs.pytest.org/en/5.4.3/example/pythoncollection.html)
* [Assertions in pytest](https://docs.pytest.org/en/stable/assert.html)
* [Assertions about expected exceptions](https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions)
* [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Python code style](https://docs.python-guide.org/writing/style/)
* [Python’s “with” statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)
* [pytest parameters](https://docs.pytest.org/en/stable/parametrize.html#parametrize-basics)
* [More pytest parameters](https://docs.pytest.org/en/stable/example/parametrize.html#paramexamples)
* [Don’t Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
* [Python decorators](https://realpython.com/primer-on-python-decorators/)
* [Aspect-Oriented Programming](https://en.wikipedia.org/wiki/Aspect-oriented_programming)
* [Hypothesis](https://hypothesis.readthedocs.io/en/latest/)
* [Python classes](https://docs.python.org/3/tutorial/classes.html)
* [Good pytest integration practices](https://docs.pytest.org/en/stable/goodpractices.html)
* [Python property decorator](https://www.programiz.com/python-programming/property)
* [tox](https://tox.readthedocs.io/en/latest/)
* [Arrange-Act-Assert](https://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html)
* [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)
* [DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
* [Dependency injection](https://en.wikipedia.org/wiki/Dependency_injection)
* [conftest.py](https://docs.pytest.org/en/2.7.3/plugins.html)
* [Python generators](https://realpython.com/introduction-to-python-generators/)
* [pytest - Usage](https://docs.pytest.org/en/2.8.7/usage.html)
* [pytest - Configuration](https://docs.pytest.org/en/latest/customize.html)
* [pytest - Configuration Options](https://docs.pytest.org/en/latest/reference.html#ini-options-ref)
* [pytest - Usage](https://docs.pytest.org/en/2.8.7/usage.html)
* [pytest - Configuration](https://docs.pytest.org/en/latest/customize.html)
* [pytest - Configuration Options](https://docs.pytest.org/en/latest/reference.html#ini-options-ref)
* [pytest - Working with custom markers](https://docs.pytest.org/en/stable/example/markers.html)
* [pytest - Marking test functions with attributes](https://docs.pytest.org/en/stable/mark.html)
* [pytest - testpaths](https://docs.pytest.org/en/latest/reference.html#confval-testpaths)
* [Requests: HTTP for Humans](https://requests.readthedocs.io/en/master/)
* [DuckDuckGo API](https://duckduckgo.com/api)
* [Tavern API Testing](https://tavern.readthedocs.io/en/latest/)
* [pytest - Installing and using plugins](https://docs.pytest.org/en/latest/plugins.html)
* [pytest - Writing plugins](https://docs.pytest.org/en/latest/writing_plugins.html)
* [Selenium WebDriver with Python](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
* [pytest-bdd](https://github.com/pytest-dev/pytest-bdd)
* [pytest-html](https://github.com/pytest-dev/pytest-html)
* [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/index.html)
* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.1/)
* [pytest - xdist distributed testing plugin](https://docs.pytest.org/en/3.0.1/xdist.html)
* [Automation Panda - A Guide to Parallel Testing](https://automationpanda.com/2018/01/21/to-infinity-and-beyond-a-guide-to-parallel-testing/)
