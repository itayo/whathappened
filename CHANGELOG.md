# Changelog

## v0.3.0 (2020-10-19)

### Docs

* Changelog - update to v0.3.0

### Features

* Add basic command line options [BREAKING]

### Fixes

* Gracefully handle commits like 'filename.py: message'
* Increase robustness of scope by allowing spaces, dots, etc.


## v0.2.0 (2020-10-18)

### Docs

* Changelog - update for v0.2.0
* Readme - add command-line indicator to installation instructions
* Readme - add commit message examples
* Readme - add more details about message types
* Readme - link badges to sensible destinations

### Features

* Add command line script
* Detect and handle breaking changes
* Group commits by version [BREAKING]
* Group commits in each version by type

### Fixes

* Add appropriate capitalisation to changelog items
* Only display user-relevant commits types in the changelog
* Remove extra line at end of changelog


## v0.1.1 (2020-10-18)

### Docs

* Changelog - update for v0.1.1
* Readme - add Python version badge
* Readme - add installation, execution, and changelog instructions
* Readme - move broken 'commits since' badge


## v0.1.0 (2020-10-17)

### Docs

* Changelog - add initial CHANGELOG.md
* Git_commits - add credit to original source
* Readme - add badges
* Readme - add inspiration
* Readme - specify expected message format

### Features

* Add changelog generation script
* Add git_commits.py from existing Gist
* Create example.py

### Other

* Initial commit

### Refactorings

* Git_commits - convert to Python3
