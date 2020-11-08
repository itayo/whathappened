from whathappened import changelog as cl
from whathappened.git_commits import get_commits


def main():
    commits = get_commits()
    versions = cl.compile_log(commits)
    versions = cl.update_latest_version(versions, prefix='v')
    log = cl.format_log(versions)
    cl.write_log(log, "CHANGELOG.md")


if __name__ == '__main__':

    main()
