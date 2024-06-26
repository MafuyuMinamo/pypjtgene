# Python project generator

## Overview

概要

- このモジュールは、『プロジェクト名と保存先のパスを渡せば、あとは自動でPythonプロジェクトのディレクトリ構成を生成してくれる仕組み』を提供します。

- オプション機能

  - Python仮想環境の構築（python -m venv）

  - Gitによるリポジトリの初期セットアップ（git init）

- プロジェクト名、保存先のパスは、組み込み関数のinput()、または、TkinterやStreamlitのようなGUIを使って事前に取得しておきましょう。

```text
生成されるプロジェクトのディレクトリ構成

プロジェクト名：my_project
保存先のパス：parent_directory

<parent_directory>
　└<my_project>
　　├<.git> (option)
　　├<.venv> (option)
　　├README.md
　　├pyproject.toml
　　├LICENSE
　　├<docs>
　　├<logs>
　　├<my_project>
　　│　├<config>
　　│　├my_project.py
　　│　└__init__.py
　　└[tests]
　　　　└test_my_project.py
```

## Usage

使い方

### Installation

インストール方法

`pip install git+https://github.com/MafuyuMinamo/pypjtgene.git`

### class / method / function

#### class ProjectGenerator

##### `set_parent_dir_path`

- summary
  - プロジェクトを保存するフォルダ（親フォルダ）のパスを取得する

- Args
  - parent_dir_path (str): プロジェクトを保存するフォルダのパス

- returns
  - bool: 有効なパスなら True

##### `set_project_name`

- summary
  - プロジェクト名を取得する

- Args
  - pj_name (str): プロジェクト名

- returns
  - bool: 有効なパスなら True

##### `execute`

- summary
  - プロジェクトの生成を実行する

- returns
  - bool: 成功したら True

##### `project_root_path (property)`

- summary
  - プロジェクトフォルダのパスのゲッター

##### `create_venv`

- summary
  -プロジェクトに仮想環境のインストールを行う

- Args
  - project_path (str): プロジェクトフォルダのパス
  - exec (bool, optional): 仮想環境をインストールを行う場合は True（デフォルトは True）

##### `git_init`

- summary
  - git init を実行する

- Args
  - project_path (str): プロジェクトフォルダのパス
  - exec (bool, optional): git init を実行する場合は True（デフォルトは True）

### Examples of use

コーディング例

```python
import os

from pypjtgene import ProjectGenerator


def example_pypjtgene():

    pj_name = "myproject"
    parent_dir = os.path.expanduser("~/Desktop")

    ex = ProjectGenerator()
    ex.set_project_name(pj_name)
    ex.set_parent_dir_path(parent_dir)
    ex.execute()

    pj_path = ex.project_root_path

    ex.create_venv(pj_path)
    ex.git_init(pj_path)


if __name__ == "__main__":

    example_pypjtgene()

```

### Uninstallation

アンイストール方法

`pip uninstall pypjtgene`

## Dependencies

依存関係の表記

- None
