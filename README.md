# Backup Utils

A Python utility for creating timestamped backups of Python scripts and projects.

## Installation

```bash
pip install fstrent_bkitup
```

## Usage

### Backing up a single script

Place this at the very top of your script, right after your imports:

```python
# your_script.py
import sys
import os
# ... your other imports ...

from fstrent_bkitup import backup_script

# Create backup before running the script
backup_script(__file__)

# Rest of your script below
def main():
    # your code here
    pass

if __name__ == "__main__":
    main()
```

### Backing up a project

For backing up multiple files or entire directories, use backup_project:

```python
# your_script.py
import sys
import os
# ... your other imports ...

from fstrent_bkitup import backup_project

# Create backup of script and project files before running
backup_project(
    __file__,  # current script
    additional_paths=[
        'lib',           # backup entire lib directory
        'config.json',   # backup specific files
        'src'           # backup src directory
    ],
    output_dir='backups'  # where to store the zip files
)

# Rest of your script below
def main():
    # your code here
    pass

if __name__ == "__main__":
    main()
```

## Features

- Create timestamped backups of individual Python scripts
- Create ZIP archives of entire projects including specified directories and files
- Preserve file metadata
- Configurable output directory

### Backup Naming

- Single script backups: `original_name_YYYYMMDD_HHMMSS.py`
- Project backups: `original_name_YYYYMMDD_HHMMSS.zip`

## Examples

### Basic Script Backup

```python
from fstrent_bkitup import backup_script

# Creates a backup like: myscript_20240320_143022.py
backup_script(__file__)
```

### Project Backup with Multiple Paths

```python
from fstrent_bkitup import backup_project

# Creates a zip file containing your script and all specified paths
# Example: myscript_20240320_143022.zip
backup_project(
    __file__,
    additional_paths=[
        'lib',
        'config',
        'data/important.csv'
    ],
    output_dir='backups'
)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.