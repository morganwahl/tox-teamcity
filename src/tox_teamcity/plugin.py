"""
Organizes test runs in each environment into separate "test suites".

Tox plugin for use with TeamCity.
"""


import pluggy
from teamcity.messages import TeamcityServiceMessages
from teamcity import is_running_under_teamcity

hookimpl = pluggy.HookimplMarker("tox")


_messages = TeamcityServiceMessages()


def _testsuite_name(venv):
    return venv.name


@hookimpl
def tox_runtest_pre(venv):
    if is_running_under_teamcity():
        _messages.testSuiteStarted(_testsuite_name(venv))


@hookimpl
def tox_runtest_post(venv):
    if is_running_under_teamcity():
        _messages.testSuiteFinished(_testsuite_name(venv))
