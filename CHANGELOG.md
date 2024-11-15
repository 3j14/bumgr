# Changelog

## 0.4.0

Add more verbose output to the CLI, and introduce the `Power` plugin.

### Breaking changes
- The parameters passed to `bumgr` have changed. Notably the verbosity,
log file, and the new `--no-cli` parameter now behave differently.

### Features
- The `Power` plugin skips the backup if the device is not charging
(macOS only at the moment).

## 0.3.0

Add the `--version` command line argument.

## 0.2.1

### Fixes

Fix crash when specifying a config file using the `-c` command line
argument.

## 0.2.0

This release adds the command `bumgr env` to be used with the `restic`
executable.

### Features
- Add the command `bumgr env`.

## 0.1.1

Minor changes made to the project metadata, adding a changelog, and
automating publishing of the packages to PyPI.

### Other
- Fix type hints in `bumgr.Tailscale`.

## 0.1.0

First public release of Bumgr. Includes basic features such as 'mount', 'backup'
and 'init'. Refer to the README.md file for more information on the features
of this first version.
