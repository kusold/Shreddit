# Agent Guidelines for Shreddit

## Workflow
- **NEVER commit directly to main** - always use pull requests
- **Before each commit**: Run tests with `uv run pytest tests/ -v` and only commit if all tests pass
- **Before marking PR as ready**: Build and test the Docker image with `config` directory mounted
- **Docker test command**: `container build --tag shreddit:test . && container run --rm -v $(pwd)/config:/config shreddit:test`

## Build/Test/Lint Commands
- **Install**: `uv pip install -e .`
- **Run**: `shreddit --help` or `shreddit -c path/to/shreddit.yml`
- **Test with config**: `shreddit -c config/shreddit.yml` (ensure `trial_run: True` in config for safe testing)
- **No linter configured** - follow PEP 8 style conventions

## Code Style
- **Python version**: 3.12+ (defined in pyproject.toml:20)
- **Imports**: Standard library first, third-party next, local imports last (see shreddit/app.py:1-11, shreddit/shredder.py:1-15)
- **Formatting**: 4-space indentation, no strict line length enforced
- **Naming**: snake_case for functions/variables, PascalCase for classes (e.g., `Shredder`, `ShredditError`)
- **Private attributes**: Prefix with underscore (e.g., `self._logger`, `self._username`)
- **Error handling**: Custom `ShredditError` exception for application errors (shreddit/util.py:26-31)
- **Logging**: Use `logging` module, level controlled by `verbose` config option (shreddit/shredder.py:22-24)

## Commit Convention
- **Required**: Conventional Commits format: `<type>(<scope>): <subject>` (see CONTRIBUTING.md)
- **Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
- **Breaking changes**: Add `!` after type or `BREAKING CHANGE:` in footer for major version bump
- **Validation**: PR titles must follow this convention (enforced by semantic-pr.yml workflow)
