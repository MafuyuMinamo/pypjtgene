import os
import pathlib
import subprocess

from pjtree import ProjectTree
from mylogger import MyStreamLogger

log = MyStreamLogger("DEBUG")


class ProjectGenerator:

    parent_dir_path: str | None = None
    pj_name: str | None = None
    pj_dir_path: str | None = None
    _project_root_path: str | None = None

    def __init__(self):
        pass

    @staticmethod
    def _check_invalid_character(file_name: str) -> bool:
        """ファイル名に無効文字が使用されているかを判定

        Args:
            string (str): 任意の文字列

        Returns:
            bool: 無効文字が含まれている場合は True
        """
        invalid_character = [
            "\\",
            "/",
            ":",
            "*",
            "?",
            "<",
            ">",
            "|",
            "+",
        ]
        for character in invalid_character:
            if character in file_name:
                return True
            else:
                pass
        return False

    def _check_parent_dir_path(self, parent_dir_path: str) -> bool:
        """親フォルダの存在確認

        Args:
            parent_dir_path (str): 親フォルダのパス

        Returns:
            bool: 有効なパスなら True
        """
        if os.path.isdir(parent_dir_path) is True:
            self.parent_dir_path = parent_dir_path
            return True
        else:
            log.error("指定の親フォルダは存在しません。")
            log.error(parent_dir_path)
            return False

    def set_parent_dir_path(self, parent_dir_path: str) -> bool:
        """親フォルダのパスを設定する

        Args:
            parent_dir_path (str): 親フォルダのパス

        Returns:
            bool: 有効なパスなら True
        """
        if self._check_parent_dir_path(parent_dir_path) is True:
            log.info("有効な親フォルダがセットされました。")
            return True
        else:
            return False

    def _check_pj_name(self, pj_name: str) -> bool:
        """プロジェクト名の確認

        Args:
            pj_name (str): プロジェクト名

        Returns:
            bool: 有効な名前なら True
        """
        if type(pj_name) is str:
            if self._check_invalid_character(pj_name) is False:
                self.pj_name = pj_name
                return True
            else:
                log.error("プロジェクト名に禁止文字が含まれています。")
                return False
        else:
            log.error("プロジェクト名が文字列以外の型で入力されました。")
            log.error(pj_name)
            log.error(type(pj_name))
            return False

    def set_project_name(self, pj_name: str) -> bool:
        """プロジェクト名を設定する

        Args:
            pj_name (str): プロジェクト名

        Returns:
            bool: 有効な名前なら True
        """
        if self._check_pj_name(pj_name) is True:
            log.info("有効なプロジェクト名がセットされました。")
            return True
        else:
            return False

    def _create_pj_dir(self, set_parent_dir_path: bool, set_project_name: bool) -> bool:
        """プロジェクトフォルダを作成する

        Args:
            set_parent_dir_path (function): -> bool
            set_project_name (function): -> bool

        Returns:
            bool: 作成できたら True
        """
        if set_parent_dir_path is True and set_project_name is True:
            self.pj_dir_path = os.path.join(self.parent_dir_path, self.pj_name)
            if os.path.isdir(self.pj_dir_path) is True:
                log.error("既に同じ名前のプロジェクトが存在します。")
                return False
            else:
                pathlib.Path(self.pj_dir_path).mkdir(
                    parents=True, exist_ok=True)
                log.info("プロジェクト用のフォルダを作成しました。")
                return True
        else:
            log.error("プロジェクト用のフォルダを作成できません。")
            return False

    def _generate_project(self):
        """プロジェクトにフォルダとファイルを追加する"""
        tree = ProjectTree(self.pj_name, self.pj_dir_path)
        tree.create_dirs_files()

        for dir_path in tree.pj_dirs:
            pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)

        for file_path in tree.pj_files:
            with open(file_path, mode="w") as f:
                f.write("")

        # * README.md の中身を記載
        tree.add_readme_md()

        # * pyproject.toml の中身を記載
        tree.add_pyproject_toml()

        # * .gitignore の中身を記載
        tree.add_gitignore()

    def execute(self) -> bool:
        """プロジェクトの生成を実行する

        Returns:
            bool: 成功したら True
        """
        if (
            self._create_pj_dir(
                self.set_parent_dir_path(self.parent_dir_path),
                self.set_project_name(self.pj_name),
            )
            is True
        ):
            self._generate_project()
            self._project_root_path = os.path.join(
                self.parent_dir_path, self.pj_name)
            return True
        else:
            return False

    @staticmethod
    def create_venv(project_path: str, exec: bool = True):
        """仮想環境のインストール

        Args:
            project_path (str): プロジェクトフォルダのパス
            exec (bool, optional):

                仮想環境をインストールを行う場合は True

                Defaults to True.
        """
        if exec is True:
            venv_dir_path = os.path.join(project_path, ".venv")
            cmd = r"python -m venv {}".format(venv_dir_path)
            log.info("仮想環境をインストールしています。")
            p = subprocess.Popen(cmd)
            p.wait()
            log.info("仮想環境をインストールしました。")
        else:
            log.info("仮想環境のインストールをスキップします。")

    @property
    def project_root_path(self):
        return self._project_root_path

    @property
    def is_git(self):
        cmd = "git --version"
        p = subprocess.run(cmd, encoding="utf-8", stdout=subprocess.PIPE)
        return "git version" in p.stdout

    def git_init(self, project_path: str, exec: bool = True):
        """git init を実行する

        Args:
            project_path (str): プロジェクトフォルダのパス
            exec (bool, optional):

                git init を実行する場合は True

                Defaults to True.
        """
        if exec is True:
            if self.is_git is True:
                cmd = "git init {}".format(project_path)
                log.info("git init を実行しています。")
                p = subprocess.Popen(cmd)
                p.wait()
                log.info("git init が完了しました。")
            else:
                log.info("Git がインストールされていません。処理をスキップします。")
        else:
            log.info("git init の実行をスキップします。")
