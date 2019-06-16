# JMA_grib2
気象庁提供のgrib2ファイルをパースするライブラリ。

## install
```sh
$ pipenv install JMA-grib2
```

## Usage
```python3
from jma_grib2 import Ggis1km
with open('Z__C_RJTD_20070101000000_RDR_JMAGPV_Ggis1km_Prr10lv_ANAL_grib2.bin', 'rb') as f:
    g = Ggis1km(f)
```

## サポート範囲
| 項目 | バージョン | データ詳細 |
|---|---|---|
| １kmメッシュ全国合成レーダーGPV | 0.0.4a3〜 | 気象庁が保有する全国20台の気象レーダーで観測したエコー強度の10分間隔データ |

## パッケージ開発環境関連
セットアップ:
```sh
$ pipenv install
```


.tar.gzファイル生成，公開など
```sh
$ pipenv run python3 setup.py sdist
$ ipenv run python3 -m twine upload dist/JMA_grib2-0.0.x.tar.gz
```

バージョン情報はgitのtagから生成される。
