# この記事の目的
・Atcoderでのコンテスト本番中にあたふた慌てないように整理すること
・問題を解いてる途中に参照しやすい状態にすること
・アウトプット作業に慣れること
・Markdown記法になれること
・ページ内リンクがやりたかった


【**随時更新予定**】


|目次|
|-----------------|
|[1. 入力編](#1.input)|
|[2. リスト編](#2. リスト編)|
|[3. 数値編](#3. 数値編)|
|[4. 書き方編](#4. 書き方編)|
|[5. 出力編](#5. 出力編)

#1.input
## 1.0 入力用
```python
import sys
input = sys.stdin.readline
```
これで`input()`だけより早くなるらしい
### 1.2 単入力
```python
n=int(input())
```
### 1.3 複数入力
```python
n,m=(int(x) for x in input().split())
```
### 1.4 リスト入力
```python
l = [int(i) for i in input().split()]
```
## 2. リスト編
### 2.1 0リスト,空リスト
```python
l=[0]*n
l=[]
```
### 2.2 リスト要素追加
```python
l.append(n)
```
### 2.3 リスト重複なし
```python
l=set(l)
```
### 2.4 リスト大きい順ソート
```python
l.sort(reverse=True)
```
## 3. 数値編
### 3.1 素因数分解リスト列挙
```python
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
```
### 3.2 偶数True奇数False
```python
def evenjudge(obj):
    if obj %2==0:
        return True
    else:
        return False
```
## 4. 書き方編
### 4.1 2重ループ
```python
import itertools
for i,j in itertools.product(range(n), range(n)):
    pass
```
### 4.2 リスト内組み合わせ
```python
import itertools
itertools.combinations(list,n)
```
## 5. 出力編
### 5.1 スペース間隔出力
```python
print(s,end=' ')
```
大体ループの中に入れてる
