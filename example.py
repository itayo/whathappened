from whathappened import changelog as cl
from whathappened.git_commits import get_commits


def main():
    start = None
    end = None
    commits = get_commits()
    commits = cl.filter_commits(commits, start, end)
    versions = cl.compile_log(commits)
    log = cl.format_log(versions)
    cl.write_log(log, "CHANGELOG.md")


if __name__ == '__main__':

    main()
