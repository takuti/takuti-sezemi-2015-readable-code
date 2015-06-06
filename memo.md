## メモ

### 仕様3

#### 実装

https://github.com/takuti/takuti-sezemi-2015-readable-code/commit/9f5055cba2e9179f202becd29b77d103c699e74d

#### どうしてリーダブル？

以下のように実行時引数の数をチェックし、エラー時のメッセージとして正しい実行方法を示している。おかげで、エラーハンドリングが想定している実行方法の説明を兼ねている。

```python
argc = len(sys.argv)

if argc != 2:
  sys.exit('Error: `$ python recipe.py ${recipe-filename}`')
```

#### この書き方の一言説明

自己説明的なコード？