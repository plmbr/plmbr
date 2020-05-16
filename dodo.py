from pathlib import Path
from plmbr.version import version

pys = list(Path('.').rglob('*.py'))
mds = list(Path('.').rglob('*.md'))
sdist = Path('dist') / f'plmbr-{version}.tar.gz'


def task_test():
    return {
        'actions': ['pytest -v'],
        'file_dep': pys,
    }


def task_docs():
    return {
        'actions': [
            'rm -rf docs',
            'pdoc --html -f -o pdoc --config show_source_code=False plmbr',
            'mv pdoc/plmbr docs'
        ],
        'targets': [],
        'file_dep': pys + mds,
        'task_dep': ['test'],
        'verbosity': 2,
    }


def task_build():
    return {
        'actions': ['python setup.py sdist'],
        'targets': [sdist],
        'file_dep': pys,
        'task_dep': ['test']
    }


def task_upload():
    return {
        'actions': [f'twine upload {sdist}'],
        'file_dep': [sdist],
        'verbosity': 2,
    }
