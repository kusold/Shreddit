# Changelog

All notable changes to this project will be documented in this file.

## [6.3.1](https://github.com/kusold/Shreddit/compare/v6.3.0...v6.3.1) (2025-11-02)

### Bug Fixes

* bump idna from 2.5 to 3.7 to resolve CVE-2024-3651 ([3718d94](https://github.com/kusold/Shreddit/commit/3718d949afaba8ac80bdcf200b961683352cfb6d)), closes [#91](https://github.com/kusold/Shreddit/issues/91)

### Documentation

* add AGENTS.md and update documentation for Python 3.12+ requirement ([f28cb49](https://github.com/kusold/Shreddit/commit/f28cb497ebf12b3b602e24a26d42aa87229770a8))

### Chores

* improve semantic-pr workflow documentation ([7d2a8ab](https://github.com/kusold/Shreddit/commit/7d2a8ab37db67f8be5748184b98c05110acf3352))

## [6.3.0](https://github.com/kusold/Shreddit/compare/v6.2.0...v6.3.0) (2025-11-02)

### Features

* add automated Docker security scanning with vulnerability remediation ([c06074d](https://github.com/kusold/Shreddit/commit/c06074dd32014109302cf73369aea2e0066a79fc))
* add semantic commit validation and improve vulnerability scanning ([b406878](https://github.com/kusold/Shreddit/commit/b406878fd872855478318487366ddede02e4caa6))

### Chores

* add commitlint configuration file ([c74b30e](https://github.com/kusold/Shreddit/commit/c74b30e750b57d3bb73b747909172e959c288588))

## [6.2.0](https://github.com/kusold/Shreddit/compare/v6.1.0...v6.2.0) (2025-11-02)

### Features

* add automated release workflow with semantic versioning and binary builds ([7a514a2](https://github.com/kusold/Shreddit/commit/7a514a29a3466b7dbf03545ca89d162fb380387f))
* migrate project to use uv for package management ([87f6207](https://github.com/kusold/Shreddit/commit/87f62072ddc4ee8120a1b48214812fd0491c318c))
* upgrade to Python 3.12 and add setuptools dependency ([05bc95b](https://github.com/kusold/Shreddit/commit/05bc95b2bbd59165588907040818d260849ce226))
* upgrade to Python 3.13 ([c19a2e1](https://github.com/kusold/Shreddit/commit/c19a2e174569fbb14069660358d59287039ff476))
* upgrade to Python 3.14 ([cf76248](https://github.com/kusold/Shreddit/commit/cf76248192e6fee033c18ea0bca784491b7d093f))

### Bug Fixes

* add missing appdirs dependency to pyproject.toml ([39c2066](https://github.com/kusold/Shreddit/commit/39c206654ca7f587d20f349bd85248bbad201943))
* include README.md in Dockerfile for build ([53ee142](https://github.com/kusold/Shreddit/commit/53ee1422d7630dfbd6aa8873b4fde088bb581be5))

### Documentation

* add Apple Container instructions for macOS users ([9650e5d](https://github.com/kusold/Shreddit/commit/9650e5d6f3963dd7a7223f9e72145228d1465166))

### Code Refactoring

* switch to official Python image with uv via multi-stage build ([ff5b6ba](https://github.com/kusold/Shreddit/commit/ff5b6ba57e94c81c1129ed5916b320772dc4765b))
