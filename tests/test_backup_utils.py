import os
from pathlib import Path
import pytest
from fstrent_bkitup import backup_script, backup_project

@pytest.fixture
def temp_script(tmp_path):
    script = tmp_path / "test_script.py"
    script.write_text("print('test')")
    return script

def test_backup_script(temp_script):
    backup_path = backup_script(temp_script)
    assert backup_path.exists()
    assert backup_path.name.startswith("test_script_")
    assert backup_path.suffix == ".py"

def test_backup_project(temp_script, tmp_path):
    # Create a mock project structure
    lib_dir = tmp_path / "lib"
    lib_dir.mkdir()
    (lib_dir / "helper.py").write_text("def help(): pass")
    
    backup_path = backup_project(temp_script, [lib_dir])
    assert backup_path.exists()
    assert backup_path.name.startswith("test_script_")
    assert backup_path.suffix == ".zip" 