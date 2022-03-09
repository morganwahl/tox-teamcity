import re


def test_run(initproj, cmd):
    initproj(
        "pkg123-0.7",
        filedefs={
            "tox.ini": """
                [tox]
                envlist = py, b
                skipsdist = True
                [testenv]
                setenv = TEAMCITY_VERSION = 1
                commands=python -c "print('perform')"
                [testenv:b]
            """
        },
    )
    expected_messages = [
        rf"##teamcity\[{message} timestamp='[^']*' name='{envname}'\]"
        for message in ('testSuiteStarted', 'testSuiteFinished')
        for envname in ('py', 'b')
    ]
    result = cmd()
    result.assert_success(is_run_test_env=False)
    print(result.out)
    for expected_message in expected_messages:
        assert re.search(expected_message, result.out)
