import os


class ProjectTree:

    pj_dirs: list = []
    pj_files: list = []

    def __init__(self, pj_name: str, pj_dir_path: str):

        self.pj_name = pj_name
        self.pj_dir_path = pj_dir_path

        # * 作成するフォルダのパス
        self.dir_path_docs = os.path.join(pj_dir_path, "docs")
        self.dir_path_logs = os.path.join(pj_dir_path, "logs")
        self.dir_path_tests = os.path.join(pj_dir_path, "tests")
        self.dir_path_mypj = os.path.join(pj_dir_path, pj_name)
        self.dir_path_config = os.path.join(self.dir_path_mypj, "config")

        # * 作成するファイルのパス
        self.file_path_readme = os.path.join(
            pj_dir_path,
            "README.md",
        )
        self.file_path_test = os.path.join(
            self.dir_path_tests,
            "test_" + pj_name + ".py",
        )
        self.file_path_test_init_py = os.path.join(
            self.dir_path_tests,
            "__init__.py",
        )
        self.file_path_init_py = os.path.join(
            self.dir_path_mypj,
            "__init__.py",
        )
        self.file_path_src = os.path.join(
            self.dir_path_mypj,
            pj_name + ".py",
        )
        self.file_path_toml = os.path.join(
            pj_dir_path,
            "pyproject.toml",
        )
        self.file_path_license = os.path.join(
            pj_dir_path,
            "LICENSE",
        )
        self.file_path_gitignore = os.path.join(
            pj_dir_path,
            ".gitignore",
        )
        self.file_path_dot_env = os.path.join(
            self.dir_path_config,
            ".env",
        )
        self.file_path_dot_env_example = os.path.join(
            self.dir_path_config,
            ".env.example",
        )

    def create_dirs_files(self):
        """作成するフォルダとファイルのパスのリストを作成する"""

        # * フォルダのパスリスト
        self.pj_dirs.append(self.dir_path_docs)
        self.pj_dirs.append(self.dir_path_logs)
        self.pj_dirs.append(self.dir_path_tests)
        self.pj_dirs.append(self.dir_path_mypj)
        self.pj_dirs.append(self.dir_path_config)

        # * ファイルのパスリスト
        self.pj_files.append(self.file_path_readme)
        self.pj_files.append(self.file_path_test)
        self.pj_files.append(self.file_path_test_init_py)
        self.pj_files.append(self.file_path_init_py)
        self.pj_files.append(self.file_path_src)
        self.pj_files.append(self.file_path_toml)
        self.pj_files.append(self.file_path_license)
        self.pj_files.append(self.file_path_dot_env)
        self.pj_files.append(self.file_path_dot_env_example)

    def add_readme_md(self):
        """『readme.md』の中身を記載する"""

        with open(self.file_path_readme, mode="w", encoding='utf-8') as f:
            f.write("# (Project / Module name)\n")
            f.write("\n")
            f.write("## Overview\n")
            f.write("\n")
            f.write("概要\n")
            f.write("\n")
            f.write("Work in progress.\n")
            f.write("\n")
            f.write("## Usage\n")
            f.write("\n")
            f.write("使い方\n")
            f.write("\n")
            f.write("### Installation\n")
            f.write("\n")
            f.write("インストール方法\n")
            f.write("\n")
            f.write("`Work in progress.`\n")
            f.write("\n")
            f.write("### class / method / function\n")
            f.write("\n")
            f.write("`Work in progress.`\n")
            f.write("\n")
            f.write("### Examples of use\n")
            f.write("\n")
            f.write("コーディング例\n")
            f.write("\n")
            f.write("```python\n")
            f.write("'Work in progress.'\n")
            f.write("```\n")
            f.write("\n")
            f.write("### Uninstallation\n")
            f.write("\n")
            f.write("アンインストール方法\n")
            f.write("\n")
            f.write("`Work in progress.`\n")
            f.write("\n")
            f.write("## Dependencies\n")
            f.write("\n")
            f.write("依存モジュールの表記\n")
            f.write("\n")
            f.write("- Work in progress.\n")
            f.write("\n")

    def add_pyproject_toml(self):
        """『pyproject.toml』の中身を記載する"""

        with open(self.file_path_toml, mode="w", encoding='utf-8') as f:
            f.write("[project]\n")
            f.write('name = "' + str(self.pj_name) + '"\n')
            f.write('version = "0.0.1"\n')
            f.write("\n")
            f.write("dependencies =  []\n")
            f.write("\n")
            f.write("[tool.pytest.ini_options]\n")
            f.write('pythonpath = "{}"\n'.format(str(self.pj_name)))
            f.write('testpaths = ["tests",]\n')
            f.write("\n")

    def add_gitignore(self):
        """『.gitignore』の中身を記載する"""

        with open(self.file_path_gitignore, mode="w", encoding='utf-8') as f:
            f.write("# python cache\n")
            f.write("__pycache__/\n")
            f.write("\n")
            f.write("# venv\n")
            f.write("venv/\n")
            f.write(".venv/\n")
            f.write(".env\n")
            f.write("\n")
            f.write("# test\n")
            f.write(".pytest_cache/\n")
            f.write("\n")
            f.write("# vscode\n")
            f.write(".vscode/\n")
