# Contributing to Shreddit

Thank you for your interest in contributing to Shreddit! This document provides guidelines for contributing to the project.

## Commit Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/) to automate releases and generate changelogs. All commit messages must follow this format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

- **feat**: A new feature (triggers a minor version bump)
- **fix**: A bug fix (triggers a patch version bump)
- **docs**: Documentation changes
- **style**: Code style changes (formatting, missing semi-colons, etc.)
- **refactor**: Code refactoring without changing functionality
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **build**: Changes to build system or dependencies
- **ci**: Changes to CI/CD configuration
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

### Breaking Changes

To trigger a major version bump, add `BREAKING CHANGE:` in the commit footer, or append `!` after the type:

```
feat!: remove support for Python 3.7

BREAKING CHANGE: Python 3.7 is no longer supported
```

### Examples

```
feat: add support for multi-factor authentication

This commit adds support for Reddit accounts with 2FA enabled.
```

```
fix: prevent crash when config file is missing

Adds proper error handling when shreddit.yml is not found.
```

```
docs: update installation instructions

Add instructions for installing with uv package manager.
```

```
chore: upgrade dependencies

Updates praw to 7.8.1 and other dependencies to latest versions.
```

## Pull Request Process

1. Fork the repository and create a new branch for your changes
2. Make your changes following the commit convention above
3. Test your changes locally
4. Submit a pull request with a clear description of the changes

## Development Setup

### Using uv (Recommended)

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the project in development mode
uv pip install -e .
```

### Using pip

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the project in development mode
pip install -e .
```

## Testing

Before submitting a pull request, ensure your changes work correctly:

```bash
# Run shreddit with your changes
shreddit --help

# Test with a config file
shreddit -c path/to/shreddit.yml
```

## Release Process

Releases are automated through GitHub Actions:

1. When commits are merged to the `master` branch, semantic-release analyzes the commits
2. If a release is warranted, it will:
   - Generate a changelog
   - Create a git tag
   - Update the version in `pyproject.toml`
   - Build and push Docker images
   - Build standalone binaries for multiple platforms
   - Create a GitHub release with all artifacts

## Questions?

If you have questions about contributing, feel free to open an issue for discussion.
