import os
import tempfile

from pypjtgene.pypjtgene import ProjectGenerator
from pypjtgene.mylogger import MyStreamLogger

test_log = MyStreamLogger("DEBUG")


def test_set_project_name():

    test = ProjectGenerator()

    # * プロジェクト名にstr型以外がセットされた場合は False
    ex_ng_pj_name_1 = 123
    test_log.info("プロジェクト名にstr型以外がセットされた場合")
    assert test.set_project_name(ex_ng_pj_name_1) is False

    # * プロジェクト名に禁止文字が含まれていていた場合は False
    ex_ng_pj_name_2 = "app\\sample"
    test_log.info("プロジェクト名に禁止文字が含まれていていた場合")
    assert test.set_project_name(ex_ng_pj_name_2) is False

    # * プロジェクト名が文字列で、禁止文字が含まれていなければ True
    ex_ok_pj_name = "sample"
    test_log.info("プロジェクト名が文字列で、禁止文字が含まれていない場合")
    assert test.set_project_name(ex_ok_pj_name) is True


def test_set_parent_dir_path():

    test = ProjectGenerator()

    with tempfile.TemporaryDirectory() as td:
        print(td)

        # * 有効なパスなら True
        assert test.set_parent_dir_path(td) is True

        # * 無効なパスなら False
        assert test.set_parent_dir_path(td + "abc") is False


def test_execute():

    test = ProjectGenerator()

    with tempfile.TemporaryDirectory() as td:

        # * 親フォルダ
        test_log.info(td)

        # * プロジェクト名
        mypj_name = "myproject"

        # * 有効なパスなら True
        assert test.set_parent_dir_path(td) is True

        # * 有効な名前なら True
        assert test.set_project_name(mypj_name) is True

        # * プロジェクトの作成が成功したら True
        assert test.execute() is True

        # * 実際にプロジェクトフォルダが作成されているかを確認
        assert os.path.isdir(os.path.join(td, mypj_name)) is True

        # * プロジェクトルートパスのゲッターの動作を確認
        assert os.path.join(td, mypj_name) == test._project_root_path

        # * 同じ名前のプロジェクトは作成できない
        assert test.execute() is False

        # * 仮想環境のインストール（無効）
        test.create_venv(test.project_root_path, exec=False)
        assert os.path.isdir(os.path.join(
            test.project_root_path, ".venv")) is False

        # * 仮想環境のインストール（有効）
        test.create_venv(test.project_root_path)
        assert os.path.isdir(os.path.join(
            test.project_root_path, ".venv")) is True

        # * git がインストールされている場合のテスト
        # ? インストールされていない環境では動作確認できてないけど、たぶん判別できるはず。
        if test.is_git is True:
            test_log.info("git はインストールされています。")

            # * git init の実行（無効）
            test.git_init(test.project_root_path, exec=False)
            assert os.path.isdir(os.path.join(
                test.project_root_path, ".git")) is False

            # * git init の実行（有効）
            test.git_init(test.project_root_path)
            assert os.path.isdir(os.path.join(
                test.project_root_path, ".git")) is True
