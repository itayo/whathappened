import pytest

from whathappened import changelog as cl


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            [
                {
                    'hash': 'e324c324df48a76113ad9b3c0887f161324046e4',
                    'tags': ['v0.1.1'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 17:30:25 2020 +0200',
                    'message': '',
                    'title': 'feat (readme): specify expected message format',
                },
                {
                    'hash': '7b4e7e657f9e3f2f4033cc5f47bcc637f5799fe9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:48 2020 +0200',
                    'message': '',
                    'title': 'fix (readme): add inspiration',
                },
                {
                    'hash': 'f60445bba0ac48e12ce6be5526644037234ae500',
                    'tags': ['v0.0.1'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 15:00:31 2020 +0200',
                    'message': '',
                    'title': 'docs (readme): add badges',
                },
                {
                    'hash': '9e57ba91f54244af913931c017480a39605c15f9',
                    'tags': [],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 13:55:04 2020 +0200',
                    'message': (
                        'Setup Python 3.6 on ubuntu-latest\n'
                        'Install pipenv and dependencies\n'
                        'Test'
                    ),
                    'title': 'build(actions): create python-app.yml for github actions',
                },
                {
                    'hash': '4094d22846daea951c4fe0d74abb2a798e9a3404',
                    'tags': ['v0.0.0'],
                    'author': 'Rollcloud <Rollcloud@users.noreply.github.com>',
                    'date': 'Sat Oct 17 13:19:28 2020 +0200',
                    'message': '',
                    'title': 'Initial commit',
                },
            ],
            """# Changelog


## v0.1.1 (2020-10-17)

* readme - specify expected message format
* readme - add inspiration


## v0.0.1 (2020-10-17)

* readme - add badges
* actions - create python-app.yml for github actions


## v0.0.0 (2020-10-17)

* Initial commit
""",
        )
    ],
)
def test_changelog(test_input, expected):
    start = None
    end = None
    commits = test_input
    commits = cl.filter_commits(commits, start, end)
    versions = cl.compile_log(commits)
    log = cl.format_log(versions)

    print(log)

    assert log == expected
