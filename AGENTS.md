# Agent Guidelines for Shreddit

## Workflow
- **NEVER commit directly to main** - always use pull requests
- **Before each commit**: 
  1. Run linter with `uv run ruff check .` and fix any issues
  2. Run tests with `uv run pytest tests/ -v` and only commit if all tests pass
- **After each push**: If there is an active PR for the branch, update the PR description to reflect all changes made since diverging from main. Use `gh pr edit <number> --body "..."` to keep the description current.
- **Before marking PR as ready**: Build and test the Docker image with `config` directory mounted
- **Docker test command**: `container build --tag shreddit:test . && container run --rm -v $(pwd)/config:/config shreddit:test`

## Build/Test/Lint Commands
- **Install**: `uv pip install -e .`
- **Install dev dependencies**: `uv pip install -e ".[dev]"`
- **Run**: `shreddit --help` or `shreddit -c path/to/shreddit.yml`
- **Test with config**: `shreddit -c config/shreddit.yml` (ensure `trial_run: True` in config for safe testing)
- **Lint**: `uv run ruff check .` (check for issues), `uv run ruff check --fix .` (auto-fix issues)
- **Test**: `uv run pytest tests/ -v`

## Code Style
- **Python version**: 3.12+ (defined in pyproject.toml:20)
- **Linter**: Ruff configured in pyproject.toml with line length 120, Python 3.12+ target
- **Imports**: Standard library first, third-party next, local imports last (automatically sorted by ruff)
- **Formatting**: 4-space indentation, maximum line length 120 characters (enforced by ruff)
- **Naming**: snake_case for functions/variables, PascalCase for classes (e.g., `Shredder`, `ShredditError`)
- **Private attributes**: Prefix with underscore (e.g., `self._logger`, `self._username`)
- **Error handling**: Custom `ShredditError` exception for application errors (shreddit/util.py:26-31)
- **Logging**: Use `logging` module, level controlled by `verbose` config option (shreddit/shredder.py:22-24)

## Commit Convention
- **Required**: Conventional Commits format: `<type>(<scope>): <subject>` (see CONTRIBUTING.md)
- **Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert
- **Breaking changes**: Add `!` after type or `BREAKING CHANGE:` in footer for major version bump
- **Validation**: PR titles must follow this convention (enforced by semantic-pr.yml workflow)
