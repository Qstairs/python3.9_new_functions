# python3.9_new_functions

## Python 3.9の新規機能

- `dict`の連結演算子`|`追加
    - `dict`型の連結が容易に
- `srt`に`removeprefix`関数追加
    - 文字列の先頭単語の削除が容易に
- `str`に`removesuffix`関数追加
    - 文字列の末尾単語の削除が容易に
- 標準ライブラリに`ZoneInfo`追加
    - タイムゾーン変換のためにライブラリのインストールが不要に

## test code
- `test.py`
    - Python 3.8以下の場合の処理と3.9の場合の処理を比較

### run
```shell
pip install pytest
pytest test.py
```
