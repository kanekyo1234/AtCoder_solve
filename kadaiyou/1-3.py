import collections

def find_unique_number(data):#3のコード　所要時間3分
    data = list(map(int, data.split()))
    data = collections.Counter(data)#今回はカウンターを用いて今回の一つだけ違う値以外にも適用可能なコードにするためdataのすべてを検索している
    return data.most_common()[::-1][0][0]#dataからvalueの値が一番小さいキーを取り出している。

def format_word(word):#2のコード　所要時間2分
    ans = ""
    box = "" #ansに入れた際の文字を記録しておく状態保存用変数
    for i in range(len(word)):
        now = word[i:i+1]
        if box != now:#ここで一個前の文字が同じじゃない場合ansに回答を入れていく
            ans += now
            box = now
    return ans

def shortest_word(word):#1のコード　所要時間1分
    length = []#長さの値を保存しておくリスト
    word = list(word.split())
    for i in word:
        length.append(len(i))#それぞれの単語の長さを入れていく
    return min(length)#その中で一番小さい値を返す

def main():
    #3番までのコードは入力値が同じなのでinputデータ自体を最初に入れておくことにする。もしそれぞれの関数ごとに入力値を指定する場合は引数なしで呼び出し
    data = input()
    # print(shortest_word(data))
    # print(format_word(data))
    # print(find_unique_number(data))
    # 1~3番までの関数のコメントアウト


if __name__ == "__main__":
    main()
