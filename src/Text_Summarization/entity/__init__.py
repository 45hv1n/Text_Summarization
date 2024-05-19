from dataclasses import dataclass
from pathlib import Path

### Entity for data ingestion confiuration
@dataclass(frozen= True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_dir_file: Path
    unzip_dir: Path

@dataclass(frozen= True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path
    ALL_FILES_REQUIRED: list