from dataclasses import dataclass
from pathlib import Path

### Entity for data ingestion confiuration
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_dir_file: Path
    unzip_dir: Path