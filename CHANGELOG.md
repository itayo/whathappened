# Changelog

## v0.3.4 (2020-11-28)

### Docs

* Changelog - updated to v0.3.4

### Features

* Changelog - implement emoji headings

### Fixes

* Changelog - do not display Other if it is the only version heading
* Changelog - escape underscores for correct Markdown rendering

### Refactorings

* Changelog - rename internal function sentence() -> \_sentence()


## v0.3.3 (2020-11-12)

### Docs

* Changelog - updated to v0.3.3
* Readme - add command-line version prefix specifier

### Fixes

* Changelog - improve robustness of category grouping


## v0.3.2 (2020-11-08)

### Docs

* Changelog - updated to v0.3.2

### Features

* Changelog - count breaking, feature, & fix commits in each version
* Changelog - replace "HEAD" with the predicted Semver version
* Command-line - allow a version prefix to be specified

### Refactorings

* Make get\_commits() accessible from changelog module


## v0.3.1 (2020-10-19)

### Docs

* Changelog - updated to v0.3.1

### Fixes

* Ci - ignore erroneous F821 error when fetching package version


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
* Add git\_commits.py from existing Gist
* Create example.py

### Other

* Initial commit

### Refactorings

* Git_commits - convert to Python3
