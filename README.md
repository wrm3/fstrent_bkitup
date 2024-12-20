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
from fstrent_bkitup import backup_script as bks

# Creates a backup in ./bkups/myscript_20240320_143022.py
bks(__file__)

# Or specify custom backup directory
bks(__file__, output_dir='my_backups')
```

### Project Backup with Multiple Paths

```python
from fstrent_bkitup import backup_project as bkp

# Creates a zip file in ./bkups/myscript_20240320_143022.zip
bkp(
    __file__,
    additional_paths=[
        'lib',
        'config',
        'data/important.csv'
    ]
)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.