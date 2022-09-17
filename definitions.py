from pathlib import Path
import sys
def get_project_root() -> Path:
    return Path(__file__).parent


if __name__ == '__main__':
    root = str(get_project_root())
    print(f'adding root path to system path: {{root}}')
    sys.path.append(root)