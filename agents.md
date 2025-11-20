# Agent Instructions for PyPI Project

## Environment Setup

This project uses **uv** for virtual environment management.

### Virtual Environment

Before running any Python scripts or installing packages, ensure the virtual environment is active:

```bash
source .venv/bin/activate
```

### Dependency Management

- All Python dependencies must be added to `requirements.txt`
- Use `uv` for package installation and environment management
- Install dependencies with:
  ```bash
  uv pip install -r requirements.txt
  ```
- When adding new dependencies:
  1. Add the package to `requirements.txt`
  2. Install using `uv pip install <package>`

## Running the Project

1. Activate the virtual environment (see above)
2. Run the main script:
   ```bash
   python calculate_pi.py
   ```

## Development Workflow

1. Always verify the virtual environment is active before executing code
2. Add any new dependencies to `requirements.txt` with appropriate version constraints
3. Tell the user how to run the script to see the output

## Current Dependencies

See `requirements.txt` for the complete list of project dependencies.
