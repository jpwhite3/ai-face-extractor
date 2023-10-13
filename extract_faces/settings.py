from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Settings:
    source_dir: Path
    target_dir: Path
    db_path: Path
    supported_extensions: List[str]
    size: int = 224
