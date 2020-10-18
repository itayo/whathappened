from datetime import datetime
from itertools import groupby


class Version:
    def __init__(self, ref, date):
        self.ref = ref
        self.date = (
            datetime.strptime(date, "%a %b %d %H:%M:%S %Y %z")
            if isinstance(date, str)
            else date
        )  # str input format Wed Apr 22 18:58:54 2020 +0200

        self.commits = []

    def __repr__(self):
        return (
            f"Version({self.ref}," f" {self.date}," f" num_commits={len(self.commits)})"
        )


class Commit:
    def __init__(self, commit_dict):
        self.commit_dict = commit_dict

    def __getattr__(self, name):

        try:
            return self.commit_dict[name]
        except KeyError:
            if name == 'header':
                return self.title.split(': ', 1)[0]
            elif name == 'description':
                return (
                    self.title.split(': ', 1)[1] if ': ' in self.title else self.title
                )
            elif name == 'type':
                return self.header.lower().split(' ', 1)[0]
            elif name == 'scope':
                return self.header.split('(')[1][:-1] if '(' in self.header else None
            else:
                raise AttributeError(f"Attribute '{name}' not found in class Commit")

    def __repr__(self):
        return f"{self.hash[:8]} {self.title})"


def filter_commits(commits, start=None, end=None):
    """
    Returns commits from start (exclusive) to end (inclusive).
    start must occur before end
    start and end can be a tag, or hash
    """
    if start is not None:
        for idx, c in enumerate(commits):
            if start in c['tags'] or c['hash'].startswith(start):
                commits = commits[:idx]
                break

    if end is not None:
        for idx, c in enumerate(commits):
            if end in c['tags'] or c['hash'].startswith(end):
                commits = commits[idx:]
                break

    return commits


def compile_log(commits):
    """
    """

    versions = []

    # iterate through commits from latest to earliest

    # group by version
    for commit in commits:
        # make a new version if required
        if len(commit['tags']) > 0 or len(versions) == 0:
            tag = commit['tags'][0] if len(commit['tags']) > 0 else 'HEAD'
            versions.append(Version(ref=tag, date=commit['date'],))

        this_commit = Commit(commit)

        # append to current version
        versions[-1].commits.append(this_commit)

    # for version in versions:
    #     print(version)

    return versions


def format_log(versions):
    output = "# Changelog"

    headings = {
        'docs': "Docs",
        'feat': "Features",
        'fix': "Fixes",
        'perf': "Performance",
        'refactor': "Refactorings",
    }

    for version in versions:
        output += f"\n\n## {version.ref} ({version.date.isoformat()[:10]})\n"

        for key, group in groupby(
            sorted(version.commits, key=lambda x: x.type), lambda x: x.type
        ):
            if key in headings:
                output += f"\n### {headings[key]}\n\n"

                for commit in sorted(group, key=lambda x: f"{x.scope} {x.description}"):
                    scope = f"{commit.scope} - " if commit.scope else ''
                    desc = commit.description
                    output += f"* {scope}{desc}\n"

    return output


def write_log(log, filename):
    with open(filename, 'w') as f:
        f.write(log)
