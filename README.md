# polyCLI - A Python CLI for Google News

A command-line interface application built in Python to interact with the Google News service via the `gnews` library.

## Features

*   Fetch top news headlines based on configurable parameters.
*   Filter news articles by specific websites (e.g., wsj.com, apnews.com, reuters.com) or custom domains.
*   Search for news articles using keywords.
*   Configure default search parameters:
    *   Maximum number of results.
    *   Time period (e.g., `1d`, `7d`) or specific start/end dates.
    *   Country.
    *   Language.
*   Reset search parameters to their original defaults.

## Requirements

*   Python 3.13
*   Dependencies listed in [`requirements.txt`](/workspaces/polycli/requirements.txt):
    *   `gnews`
    *   `pysqlite3` (Note: `libsqlite3-dev` is installed in the Docker container)

## Setup and Usage

This project is configured to run within a VS Code Development Container.

1.  **Prerequisites:** Docker installed and running. VS Code with the "Dev Containers" extension.
2.  **Open in Container:** Open the project folder in VS Code and use the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) to run "Dev Containers: Reopen in Container".
3.  **Automatic Start:** The application (`polycli.py`) is automatically executed when the container starts, as defined by the `postStartCommand` in [`.devcontainer/devcontainer.json`](/workspaces/polycli/.devcontainer/devcontainer.json).
4.  **Interact:** Follow the prompts in the integrated terminal to use the application.

### Dev Container Specifics

*   **GitHub Authentication:** The container includes the GitHub CLI (`gh`). The `devcontainer.json` configuration runs `gh auth login` during container initialization (`postStartCommand`).
    *   This command will attempt to authenticate the GitHub CLI. If you haven't authenticated `gh` using the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.

## Development Environment

The development container ([`.devcontainer/Dockerfile`](/workspaces/polycli/.devcontainer/Dockerfile)) provides a consistent environment with:

*   Python 3.13
*   Required Python packages installed via `pip`.
*   Essential build tools (`build-essential`, `libsqlite3-dev`).
*   Common utilities (`git`, `curl`, `wget`, `htop`, `sudo`, etc.).
*   GitHub CLI (`gh`).
*   Goose and Aider CLIs for AI code agent functionality.

## License

This project is licensed under the [MIT License](/workspaces/polycli/LICENSE).

## Contributing

### Disclaimer: Unmaintained and Untested Code

Please note that this program is not actively maintained or tested. While it may work as intended, it's possible that it will break or behave unexpectedly due to changes in dependencies, environments, or other factors.

Use this program at your own risk, and be aware that:
1. Bugs may not be fixed
1. Compatibility issues may arise
1. Security vulnerabilities may exist

If you encounter any issues or have concerns, feel free to open an issue or submit a pull request.