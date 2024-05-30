# Python project generator

## Overview

- このモジュールは、『プロジェクト名と保存先のパスを渡せば、あとは自動でPythonプロジェクトのディレクトリ構成を生成してくれる仕組み』を提供します。

- オプション機能

  - Python仮想環境の構築（python -m venv）

  - Gitによるリポジトリの初期セットアップ（git init）

- プロジェクト名、保存先のパスは、標準モジュールのinput関数、または、TkinterやStreamlitのようなGUIを使って事前に取得しておきましょう。

## Usage

### Installation

pip install git+https://github.com/MafuyuMinamo/pypjtgene.git

### function / method

#### class ProjectGenerator

##### set_parent_dir_path

プロジェクトを保存するフォルダ（親フォルダ）のパスを取得する

- Args
  - parent_dir_path (str): プロジェクトを保存するフォルダのパス

- returns
  - bool: 有効なパスなら True

##### set_project_name

プロジェクト名を取得する

- Args
  - pj_name (str): プロジェクト名

- returns
  - bool: 有効なパスなら True

##### execute

プロジェクトの生成を実行する

- returns
  - bool: 成功したら True

##### project_root_path (property)

プロジェクトフォルダのパスのゲッター

##### create_venv

プロジェクトに仮想環境のインストールを行う

- Args
  - project_path (str): プロジェクトフォルダのパス
  - exec (bool, optional): 仮想環境をインストールを行う場合は True（デフォルトは True）

##### git_init

git init を実行する

- Args
  - project_path (str): プロジェクトフォルダのパス
  - exec (bool, optional): git init を実行する場合は True（デフォルトは True）

### Examples of use

Work in progress.

### Uninstallation

pip uninstall pypjtgene

## Dependencies

Work in progress.
