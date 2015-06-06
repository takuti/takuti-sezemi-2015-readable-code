## 仕様3 & 4

### その1

#### 実装

https://github.com/takuti/takuti-sezemi-2015-readable-code/commit/9f5055cba2e9179f202becd29b77d103c699e74d

#### どうしてリーダブル？

以下のように実行時引数の数をチェックし、エラー時のメッセージとして正しい実行方法を示している。おかげで、エラーハンドリングが想定している実行方法の説明を兼ねている。

```python
argc = len(sys.argv)

if argc != 2:
  sys.exit('Error: `$ python recipe.py ${recipe-filename}`')
```

また、openではReadであれば `r` の指定を省略できるが、あえて省略しないことでファイル読み込みであることを明示している。

```python
open(recipe_filename, 'r')
```

#### 一言説明

自己説明的なコード？

### その2

#### 実装

https://github.com/takuti/takuti-sezemi-2015-readable-code/commit/ae957ed94b5832823db06ab81d2f578695880a33

#### どうしてリーダブル？

ファイルの読み書きは `with` を使って以下のように書くことができる。

```python
with open(recipe_filename, 'r') as f:
  # cut the tail '\n', and create recipe list
  recipes = map(lambda recipe: recipe.rstrip(), f.readlines())
  for r in recipes:
    print r
```

しかし、try-exceptによるファイル読み込み時の例外処理を実装するとネストが深くなってしまうので、あえて丁寧にファイルオープンをする。

```python
try:
  f = open(recipe_filename, 'r')
  # cut the tail '\n', and create recipe list
  recipes = map(lambda recipe: recipe.rstrip(), f.readlines())
  for r in recipes:
    print r
except IOError:
  print 'IOError: file `%s` does not exist' % recipe_filename
```

#### 一言説明

ネストを浅くする

### その3

#### 実装

https://github.com/takuti/takuti-sezemi-2015-readable-code/commit/3622438f137da8e4028e4fd63a01859d013cff13

#### どうしてリーダブル？

個人開発ではファイルポインタは `f` などという慣例的な変数名をつけがちだが、今回は以下のように変数名が何を指しているか分かることを意識した。

```python
recipe_file = open(recipe_filename, 'r')
```

また、対応する変数同士の命名に英語的な意味を含ませることで対応をクリアにした。

1. `recipe_filename` のファイルポインタは `recipe_file`
2. `recipes` のイテレーション変数は `recipe`

#### 一言説明

自己説明的な変数名