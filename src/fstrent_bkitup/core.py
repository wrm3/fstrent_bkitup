import os
import shutil
from datetime import datetime
import zipfile
from typing import List, Optional, Union
from pathlib import Path

def backup_script(script_path: Union[str, Path], output_dir: Optional[Union[str, Path]] = None) -> Path:
    """
    Create a timestamped backup of a single script file.
    
    Args:
        script_path: Path to the script file to backup
        output_dir: Directory to store backup (defaults to 'bkups' in script directory)
        
    Returns:
        Path to the created backup file
    """
    script_path = Path(script_path).absolute()
    if not script_path.is_file():
        raise FileNotFoundError(f"Script file not found: {script_path}")
        
    # Default to 'bkups' directory in script's location
    output_dir = Path(output_dir) if output_dir else script_path.parent / 'bkups'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{script_path.stem}_{timestamp}{script_path.suffix}"
    backup_path = output_dir / backup_name
    
    shutil.copy2(script_path, backup_path)
    print(f"Backup created at: {backup_path}")
    
    return backup_path

def backup_project(
    base_script_path: Union[str, Path], 
    additional_paths: Optional[List[Union[str, Path]]] = None,
    output_dir: Optional[Union[str, Path]] = None
) -> Path:
    """
    Backup a script and related project files into a zip archive.
    
    Args:
        base_script_path: Path to the main script file
        additional_paths: List of additional paths to include in backup
        output_dir: Directory to store backup (defaults to 'bkups' in script directory)
        
    Returns:
        Path to the created zip archive
    """
    base_script_path = Path(base_script_path).absolute()
    if not base_script_path.is_file():
        raise FileNotFoundError(f"Script file not found: {base_script_path}")
        
    project_dir = base_script_path.parent
    output_dir = Path(output_dir) if output_dir else project_dir / 'bkups'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{base_script_path.stem}_{timestamp}.zip"
    backup_path = output_dir / backup_name
    
    additional_paths = [Path(p).absolute() for p in (additional_paths or [])]
    
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # Add the main script
        backup_zip.write(base_script_path, arcname=base_script_path.name)
        
        # Add additional paths
        for path in additional_paths:
            if path.is_file():
                arcname = path.relative_to(project_dir)
                backup_zip.write(path, arcname=arcname)
            elif path.is_dir():
                for file_path in path.rglob('*'):
                    if file_path.is_file():
                        arcname = file_path.relative_to(project_dir)
                        backup_zip.write(file_path, arcname=arcname)
    
    print(f"Backup archive created at: {backup_path}")
    return backup_path 