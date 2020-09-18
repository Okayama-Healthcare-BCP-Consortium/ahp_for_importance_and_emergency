階層分析法(Analytic Hierarchy Process)を用いた2軸Importance, Emergencyにおける優先業務選択補助ソフトウェア
==============================

## Target

災害時における優先業務の選定を2軸Importance, Emergencyに関する数理計画問題によってモデル化する．

## Project Organization

    .
    ├── README.md          <- プロジェクトの全体像
    ├── uploads            <- 入力データが置かれるディレクトリ
    ├── templates          <- htmlファイルのためのディレクトリ
    │   ├── index.html
    │   └── result.html
    ├── ahp.py             <- AHPのモジュール
    └── main.py            <- メインプログラム

## Usage

### Step1

[Docker](https://www.docker.com/) で環境を作成します．事前に[公式ドキュメント](https://docs.docker.com/)を参照しローカル環境にDockerを導入してください．以下はDockerがインストールされており，DockerHubのアカウントを持っていることを想定しています．

### Step2

以下のコマンドをターミナルで実行して下さい．
```shell
git clone git@github.com:Okayama-Healthcare-BCP-Consortium/ahp_for_importance_and_emergency.git
```

### Step3

main.pyのあるディレクトリに移動して下さい．

### Step4

以下のコマンドをターミナルで実行して下さい．
```shell
docker pull kunifuohbc/ohbc_ahp
docker run -p 3000:3000 -v $(pwd):/work --rm kunifuohbc/ohbc_ahp
```

### Step4

ブラウザに http://localhost:3000/ を入力して下さい．

### Step5

以下のデモのように結果を取得できます．

![ahpdemo](https://user-images.githubusercontent.com/70554494/93549072-81bf3a00-f9a3-11ea-811f-c8a07ca0dd41.gif)

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)


