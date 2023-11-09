import math

def eqn2(a, b, c):
    """
    二次方程式の解を返す関数。
    >>> eqn2(1, -3, 2)
    [1, 2]
    >>> eqn2(1, -2, 1)
    [1]
    虚数解の時は文字列になっているが許してほしい。
    """
    D = b * b - 4 * a * c
    z = -b / (2 * a)
    if D < 0:
        D = math.sqrt(abs(D)) / (2 * a)
        return [str(z) + "+" + str(D) + "i", str(z) +  "-" + str(D) + "i"]
    D = math.sqrt(D) / (2 * a)
    return list(set([z + D, z - D]))


def p_to_i(x):
    return int(x + 0.5)


def f_to_i(x):
    if x >= 0:
        return p_to_i(x)
    else:
        return -f_to_i(-x)


def f_to_f1(x):
    return f_to_i(x*10) / 10


def ipower(x, y: int):
    """
    python標準の関数、pow()と同じ動作をする関数。ただし正の整数のみを考慮。
    >>> ipower(2, 4)
    16
    >>> ipower(10, 2)
    100
    再帰処理。x^n = x*(x^n) =x*x*(x^n)となるはず。
    """
    if y == 0:
        return 1
    return x * ipower(x, y - 1)


def f_to_f(x, n):
    """
    小数第n位で四捨五入する関数。
    >>> f_to_f(3.141592, 4)
    3.1416
    >>> f_to_f(-3.141592, 2)
    -3.14
    13と同じ要領だが、べき乗の計算に上記のipower関数を使用した。
    """
    pow = ipower(10, n)
    return f_to_i(x*pow) / pow


def f_to_f_(x, n):
    print(x + 0.5*(10**-n))
    if x >= 0:
        return round(x + 0.5*(10**-n), n)
    else:
        return round(x - 0.5*(10**-n), n)

# print(f_to_f_(-3.53448731, 6))

# print(f_to_f(-3.14159265, 4))


def is_even(x):
    """
    偶数かどうかを判定する関数。
    >>> is_even(3)
    False
    >>> is_even(2)
    True
    hkimura先生のいうところのねぎまリターン。
    もしかしたらもう少し良い言い方になっているかも？

    ちなみに...ビット演算子を使う方法もあります。
    https://qiita.com/7shi/items/41d262ca11ea16d85abc
    """
    return x % 2 == 0

# 16


def parity_():
    """
    入力された数が偶数か奇数かをプリントする関数。
    >>> 2
    >>> parity_()
    偶数です
    >>> 5
    >>> parity_()
    奇数です

    ビット演算子を使った解法。以下を参照してください。
    https://qiita.com/7shi/items/41d262ca11ea16d85abc
    """
    x = int(input())
    if x & 1 == 0:
        print("偶数です")
    else:
        print("奇数です")
# parity_()


def sign(x):
    """
    xが負ならば-1、0なら0、正ならば1を返す関数。
    >>> sign(10)
    1
    >>> sign(0)
    0
    >>> sign(-10)
    -1
    へんてこりんな解法を目指した。
    その数の絶対値で割れば1か-1になるはず。
    0は0割りになってしまうので条件外に。
    """
    if x == 0:
        return 0
    return int(x / abs(x))

# print(sign(10.245))


def is_teenage(y):
    """
    ティーンエイジャーかどうか判定する関数。
    >>> is_teenage(18)
    True
    >>> is_teenage(19.98)
    True
    20歳未満はティーンエイジャーだよね、ってことです。
    この解法、パクってるんですが、よくできてるなと思います。
    """
    return 13 <= int(y) <= 19


def is_triangle(x, y, z):
    """
    条件を満たす三角形が存在するかどうか判定する関数。
    >>> is_triangle(1,2,3)
    False
    >>> is_triangle(1,1,1)
    True
    x, y, z全て0以上かつ、問題文の条件を満たすようにする。
    一番長くなくても、ある辺の長さはそのほか二辺の長さより短くなるはず。
    このコードが綺麗かって言われると、個人的にはちょっと首をかしげる。
    """
    return x > 0 and y > 0 and z > 0 and x+y > z and y+z > x and z+x > y

# print(is_triangle(1/2, 1/3, 1/6))


def is_normal_triangle(x, y, z):
    """
    直角三角形が存在するか判定する関数。
    >>> is_normal_triangle(5, 12, 13)
    True
    >>> is_normal_triangle(1, 1, 1)
    False
    19の条件に加え、ピタゴラスの定理を利用。
    x^2等の計算を複数回するので、変数x2等にまとめたほうが処理が楽なはず。
    """
    x2 = x * x
    y2 = y * y
    z2 = z * z
    return is_triangle(x, y, z) and (x2 + y2 == z2 or y2 + z2 == x2 or z2 + x2 == y2)


def era(year):
    """
    西暦と和暦を変換する関数
    >>> era(1926)
    昭和元年
    >>> era(1988)
    昭和63年
    補助関数era_aux(syear, year)で年計算部分を減らした。
    例外処理もオマケで追加。
    """
    if 1926 <= year <= 1988:
        return '昭和' + era_aux(1926, year) + '年'
    if 1989 <= year <= 2018:
        return '平成' + era_aux(1989, year) + '年'
    if 2019 <= year:
        return '令和' + era_aux(2019, year) + '年'
    else:
        raise Exception("その年の和暦は大正以前の元号です。")


def era_aux(syear, year):
    """
    era(year)の補助関数。
    令和〇〇年の〇〇の部分を返す。

    文字列への変換と、基準年は元とするところがポイント。
    """
    dyear = year - syear
    if dyear == 0:
        return '元'
    else:
        return str(dyear+1)


def is_leap(year):
    """
    その年が閏年かどうか判定する関数。
    >>> is_leap(2000)
    True
    >>> is_leap(2004)
    True
    大きい数から判定したほうがはやいはず。
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def time_to_int(hh, mm, ss):
    """
    一日の何秒目かを返す関数。
    >>> time_to_int(12, 34, 56)
    45296
    >>> time_to_int(23, 59, 59)
    86399
    25時とは口頭では言わないこともないが、コンピュータ的にはないので例外としてはじく。
    """
    if 0 <= hh <= 24 and 0 <= mm <= 60 and 0 <= ss <= 60:
        return (hh * 60 + mm) * 60 + ss
    raise Exception("その時間は存在しません。")


def sec_between(h1, m1, s1, h2, m2, s2):
    """
    1と2の間の時間を返す関数。
    >>> sec_between(0, 0, 0, 23, 59, 59)
    86399
    >>> sec_between(0, 0, 0, 0, 0, 1)
    1
    テストコードの例外は、time_to_intで処理しているから不要。
    """
    return time_to_int(h2, m2, s2) - time_to_int(h1, m1, s1)


def days(m1, d1, m2, d2):
    """
    m1月d1日からm2月d2日までの日数を返す関数。
    >>> days(1, 1, 1, 1)
    0
    >>> days(12, 31, 1, 1)
    -364
    月の日数は規則性がないので、リストにして処理。
    リストは0番目からなので最初に0をつけるか、m1から1引くかどちらかをする必要がある。
    update : 不要な変数deld1とdeld2を削除。
    """
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    return sum(months[0:m2]) + d2 - sum(months[0:m1]) - d1


def days_between(y1, m1, d1, y2, m2, d2):
    """
    y1 年 m1 月 d1 日から y2 年 m2 月 d2 月までの日数を返す関数。
    >>> days_between(2022,1,1,2023,1,1)
    365
    >>> days_between(1962,3,31,2022,10,14)
    22112
    補助関数days_between_aux()に丸投げ。
    """
    return days_between_aux(y1, m1, d1, y2, m2, d2, 0)


def days_between_aux(y1, m1, d1, y2, m2, d2, ddays):
    """
    days_between()の補助関数。
    再帰的に呼び出している。
    """
    if y1 == y2:
        return ddays + days(m1, d1, m2, d2)
    if is_leap(y1):
        ddays += 1
    ddays += 365
    return days_between_aux(y1 + 1, m1, d1, y2, m2, d2, ddays)


def sum_int(n, m):
    """
    nからmまでの和を求める関数。
    >>> sum_int(0, 10)
    55
    >>> sum_int(-10, 10)
    0
    そんなに大きな数がテストコードにないので普通の再帰で。
    大きな数だったら末尾再帰のほうがベター。
    """
    if n > m:
        return 0
    return n + sum_int(n+1, m)


def sum2(n, m):
    """
    nからmまでの2乗和を求める関数。
    >>> sum2(0, 10)
    385
    >>> sum2(100, 200)
    2358350
    そんなに大きな数がテストコードにないので普通の再帰で。
    大きな数だったら末尾再帰のほうがベター。
    """
    if n > m:
        return 0
    return n*n + sum2(n+1, m)


def sum_evens(n, m):
    """
    nからmまでの偶数和を求める関数。
    >>> sum_evens(0, 100)
    2550
    >>> sum_evens(1, 101)
    2550
    頭を偶数にそろえて補助関数に丸投げ。
    """
    if not is_even(n):
        return sum_evens_aux(n+1, m)
    return sum_evens_aux(n, m)


def sum_evens_aux(n, m):
    """
    sum_int(n, m)とやっていることは一緒。
    2ずつ足しているだけ。
    """
    if n > m:
        return 0
    return n + sum_int(n+2, m)


def fz(n):
    """
    3の倍数、5の倍数、15の倍数、それ以外を判別する関数。
    >>> fz(10)
    5
    >>> fz(15)
    8
    該当しているときに足していく方式。
    """
    ans = 0
    if n % 3 == 0:
        ans += 3
    if n % 5 == 0:
        ans += 5
    return ans


def sum_fz(n, m):
    """
    fz(n)からfz(m)の和を求める関数。
    >>> sum_fz(0, 2)
    8
    >>> sum_fz(0, 10)
    27
    sum_int(n, m)と同じ要領。
    """
    if n > m:
        return 0
    return fz(n) + sum_fz(n + 1, m)


def sun_tzu():
    """
    孫子の問題(改)を考える関数。
    初期値を一番大きい数+その余りにする。
    さらに、7537刻みにすれば考える数がかなり減るはず。
    答えは22309523
    """
    num = 7537 + 3
    while True:
        if num % 557 == 2 and num % 31 == 1:
            return num
        num += 7537


def mean(xs):
    """
    リストの平均値を求める関数。
    >>> mean(range(10))
    4.5
    >>> mean([1])
    1.0
    リストの和をリスト長で割ればちょうどいいはず。
    """
    return sum(xs) / len(xs)


def median(xs):
    """
    値の中央値を返す関数
    >>> median([3])
    3
    >>> median([3, 4])
    3.5
    リストの長さが偶数の時は前後の平均を、奇数なら中央の値を取得する。
    """
    llen = len(xs)
    if is_even(llen):
        return (xs[int((llen / 2) - 1)] + xs[int((llen / 2))]) / 2
    return xs[int((llen - 1) / 2)]


def mode(xs):
    """
    リストxsの最頻値を求める関数。
    >>> mode([10])
    10
    >>> mode(["a","b","c","d","b"])
    "b"
    リストの要素名を格納するリストlstと、その登場回数を記録するリストcntを用意する。
    ただし、lstとcntの順番は対応している。
    xsのi番目の要素がlst内に存在すれば、その要素に対応するcntを1増やす。
    存在しなければ、各リストの末尾にその要素とカウント1を登録する。
    最後に、cntの最大値のインデックスを抜き出し、リストに対応させたものを出力する。

    **注意**
    本来、このような2つの要素は二重リストにして解決すべきである。
    このような書き方はバグを内包する可能性が高いので避けるべき。
    """
    lst = []
    cnt = []
    for i in xs:
        if i in lst:
            cnt[lst.index(i)] += 1
        else:
            lst.append(i)
            cnt.append(1)
    print(lst)
    print(cnt)
    return lst[cnt.index(max(cnt))]


def reverse_str(s):
    """
    文字列を反転して出力する関数。
    >>> reverse_str("abcdef")
    fedcba
    >>> reverse_str("しんぶんし")
    しんぶんし
    pythonにおいては、文字列はリストとしてとらえることができる。
    残りは末尾の文字から順に再帰。
    """
    if s == "":
        return ""
    return s[-1] + reverse_str(s[0:len(s)-1])


def find_char(s, c):
    """
    文字列sに含まれる文字cをリストで返す関数。
    >>> find_char("apple", 'p')
    ['p', 'p']
    >>> find_char("orange", 'z')
    []
    補助関数find_char_auxに丸投げ。
    """
    return find_char_aux(s, c, [])


def find_char_aux(s, c, xs):
    """
    find_charの補助関数。
    なんだか再帰の良さが失われている気がするが...
    sの一番最初の要素がcか判定して、xsに追加したりしなかったり。
    """
    if s == "":
        return xs
    if s[0] == c:
        xs.append(c)
    return find_char_aux(s[1:], c, xs)


def count_char(s, c):
    """
    文字列sに含まれる文字cの数を返す関数。
    >>> find_char("apple", 'p')
    2
    >>> find_char("orange", 'z')
    0
    38で使用したものを再利用できるかな～ってことが鍵なのかな？
    """
    return len(find_char(s, c))


def count_words(s):
    """
    文字列sの単語数を返す関数。
    >>> count_words('  ')
    0
    >>> count_words('I love you. I need you.')
    6
    splitを使うのは反則かな...?
    """
    return len(s.split())


def initial(s):
    """
    イニシャルを返す関数。
    >>> initial("Kimura TAKUYA")
    "KT"
    >>> initlal("ONEWORD")
    "O"
    split()で書式を整理後、一番最初の文字だけ抜き出す。
    "".join()でstrがたに戻してリターン。
    """
    return "".join([i[0] for i in s.split()])


def max2(x, y):
    """
    max()の自作版関数。
    >>> max2(0, 1)
    1
    >>> max2(-1, 0)
    0
    三項演算子を使った答え。
    これくらいならこっちの方が見やすい気がする。
    """
    return x if x > y else y


def max3(x, y, z):
    """
    3つの数の最大値を返す関数。
    >>> max3(0, 1, 2)
    2
    >>> max3(-2, 0, -1)
    0
    xとyの最大値をmax2を使って求め、それとzの大きい方を返せばいいよね。
    """
    return max2(max2(x, y), z)


def max_in_list(xs):
    """
    リストの最大値を返す関数。
    >>> max_in_list([1, 2, 3])
    3
    >>> max_in_list([-10, 10, 10.25])
    10.25
    暫定で一番目を最大値として、補助関数max_in_list_auxに丸投げ
    空リストに対応するため、その時だけ例外的に処理。
    """
    if xs == []:
        return []
    return max_in_list_aux(xs[1:], xs[0])


def max_in_list_aux(xs, maxnum):
    """
    max_in_listの補助関数。
    リストが空ならばそれまでに求めた最大数を返す。
    そうでなければ、xsの最初の要素と比較し、次の数の評価を再帰的に呼び出している。
    """
    if xs == []:
        return maxnum
    if xs[0] > maxnum:
        return max_in_list_aux(xs[1:], xs[0])
    return max_in_list_aux(xs[1:], maxnum)


def maxen(xs):
    """
    リストの最大値を返す関数。
    ただし、最大値が複数ある場合はリストで返す。
    >>> maxen([1, 2, 3])
    3
    >>> maxen([-10, 10, 10.25])
    10.25
    暫定で一番目を最大値として、補助関数maxen_auxに丸投げ
    空リストに対応するため、その時だけ例外的に処理。
    """
    if xs == []:
        return []
    return maxen_aux(xs[1:], xs[0], 1)


def maxen_aux(xs, maxnum, counter):
    """
    max_in_listの補助関数。
    リストが空ならばそれまでに求めた最大数を返す。
    そうでなければ、xsの最初の要素と比較する。
    xs[0]が大きければ、それを最大値に書き換える。
    等しければ、counterを+1する。
    小さければ、そのまま.
    その後、それぞれで次の数の評価を再帰的に呼び出している。
    """
    if xs == []:
        return [maxnum] * counter
    if xs[0] > maxnum:
        return maxen_aux(xs[1:], xs[0], 1)
    elif xs[0] == maxnum:
        return maxen_aux(xs[1:], maxnum, counter + 1)
    return maxen_aux(xs[1:], maxnum, counter)





def list_randoms(n, m):
    """
    nまでの整数乱数をm個、リストで返す関数。
    >>> list_randoms(2, 3)
    >>> list_randoms(2, 3)
    [1, 1, 0]
    [0, 1, 1]
    一つ目の乱数を生成して、補助関数に丸投げ。
    """
    return list_randoms_aux(n, m - 1, [my_rand()])


def list_randoms_aux(n, m, xs):
    """
    list_randomsの補助関数。
    mを減らしていき、0になったらn未満の数にして結果をリターン。
    """
    if m == 0:
        return [nums % n for nums in xs]
    return list_randoms_aux(n, m - 1, xs + [my_rand(xs[-1])])


import random
# import sys
# sys.setrecursionlimit(15000)
# pythonのrecursionの上限が1000な関係で、most_divisors(1000)が動かない。
# recursionlimitの上限を2000に変えてあげる。許して。

def my_rand(x=0):
    """
    214783647までの数の整数乱数を生成する。
    引数を取らなければ、pythonモジュールのrandrangeを使って生成。
    一番最初の乱数を生成する方法が思いつかなかったのでとりあえず妥協。
    参考: https://qiita.com/mk668a/items/d53515817c41e22e77f0
    update: numがinfに飛んでしまうことがある。乱数を初期化して応急処置。
    """
    if x == 0:
        return random.randrange(1, 214783647)
    A = 48271
    M = 214783647
    Q = M / A
    R = M % A
    num = A * (x % Q) - R * (x / Q)
    try:
        int(num)
    except OverflowError:
        print("OVERFLOWED!", num)
        num = random.randrange(1, M)
    return int(num)


def not_found(rs, n1):
    """
    整数乱数リストrs中にみつからないn1までの整数をセットで返す関数
    ただし、存在しない場合はValueErrorとして返す。
    >>> rs = [0, 2]
    >>> not_found(rs, 2)
    {1}
    特に面白みのない解答。
    """
    ret = []
    for i in range(n1):
        if i not in rs:
            ret.append(i)
    if ret == []:
        raise ValueError("n1までの全ての数がrs内に存在します。")
    return set(ret)


def bingo(n):
    """
    1~nの重複なしランダム順のリストを返す関数。
    十分シャッフルできていない気もするが、まあいいか。
    """
    lst = [i for i in range(1, n + 1)]
    for i in range(n):
        j = my_rand(i) % n
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def monte_calro_pi(m):
    """
    モンテカルロ法に従ってpiを求める関数。
    精度は...お察し。
    xについての乱数とyについての乱数を作って、いい感じに計算。
    """
    xs = [i / 1000 - 1 for i in list_randoms(1000, m)]
    ys = [i / 1000 - 1 for i in list_randoms(1000, m)]
    cnt = 0
    for i in range(m):
        if xs[i] * xs[i] + ys[i] * ys[i] <= 1:
            cnt += 1
    return 4 * cnt / m

# print(monte_calro_pi(1000))


def integral_pi(n: int):
    """
    4/(1+x^2) (x = 0->1)の数値積分。
    n = step、何分割するか決める。
    リスト内包表現で[f(0), f(1/n), ..., f(1)]を作成したのち、
    シンプソン1/3公式に従ってf(i)をいじって、その総和をいい感じに返してあげる。
    精度は10000分割で小数第12位くらいまで正しく出る。いい感じ。
    """
    xs = [4/(1+(i/n)*(i/n)) for i in range(0, n+1)]
    for i in range(1, n):
        if i % 2 == 1:
            xs[i] *= 2
        xs[i] *= 2
    return sum(xs) / (n * 3)


def digits(n: int):
    """
    整数の桁数を返す関数。
    >>> digits(10)
    2
    >>> digits(-10)
    2
    リスト内包表現と三項演算子。
    """
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return sum([1 if i in nums else 0 for i in str(n)])


def sum_of_digits(n: int):
    """
    数字の各桁の総和を求める関数。
    >>> sum_of_digits(123)
    6
    >>> sum_of_digits(-123)
    6
    絶対値にして、その後数字を文字列としてリスト化。その総和を求める。
    """
    return sum([int(i) for i in str(max2(-n, n))])


def reverse_int(n: int):
    """
    整数を反転させた整数を返す関数。
    ただし、負の数には未対応。
    >>> reverse_int(123)
    321
    >>> reverse_int(132)
    231
    reverse_str()を使ってあげる。型変換の練習問題かな？
    """
    return int(reverse_str(str(n)))


def is_id(s: str):
    """
    学生番号か判別する関数。
    >>> is_id("200A0000")
    True
    >>> is_id("2A0A00A0")
    False
    strをintに変換するときに、文字が含まれていたらエラーを吐くはず。
    そのエラーを捕まえて、Falseにしている。
    どこかで見かけた解法。やってみたかった。
    """
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(s) != 8 or not (s[3] in dic):
        return False
    nid = s[0:2] + s[4:]
    try:
        int(nid)
    except ValueError:
        return False
    return True


def is_palindrome(s: str):
    """
    回文かどうか判定する関数。
    >>> is_palindrome("abcba")
    True
    >>> is_palindrome("abcbba")
    False
    若干インチキ味のする解答。
    """
    return s == reverse_str(s)


def is_palindrome_number(n: int):
    """
    回文数か判別する関数。
    >>> is_palindrome_number(12321)
    True
    >>> is_palindrome_number(12231)
    False
    さっきの問題にstr型にして突っ込んでいるだけ。
    """
    return is_palindrome(str(n))


def max_parindrome(f: int, t: int):
    """
    from -> toで最大の回文数を求める関数。
    >>> max_parindrome(1, 100)
    9009
    >>> max_parindrome(100, 1000)
    906609
    100以下ならそんな大したことないので全探索。
    100以上、特に1000とかに近づくと、全探索だと時間がかかる。
    なので、幅deltを定義し、その幅ごとに探っていく。
    例えば、t = 1000だったら、delt = 100ごとみたいに。
    あと当然ではあるが、一番上から探した方が手っ取り早い。
    **注意**
    場合によっては正しく最大数が出ないような書き方になっているかも。
    この関数、98*98より先に99*91を計算する。
    具体的に思いつかないが、もしかしたらどちらも回文数になるパターンが存在するかも。
    """
    t1 = t
    if t > 100:
        delt = ipower(10, digits(t)-2)
    else:
        delt = t
    while f < t:
        for i in range(t1, t1 - delt, -1):
            for j in range(t1, t1 - delt, -1):
                if is_palindrome_number(i * j):
                    return i * j
        t1 -= delt
    raise ValueError("回文数は見つかりませんでした。")


def divisors_aux(n: int, divs: list, ndiv: int):
    """
    divisorsの補助関数。
    探索をsqrt(n)までで打ち切りする。
    平方数の時は別で場合分けして処理。なんかダサい。
    """
    if ndiv * ndiv > n:
        return sorted(divs)
    elif ndiv * ndiv == n:
        divs.append(ndiv)
        return sorted(divs)
    if n % ndiv == 0:
        return divisors_aux(n, divs + [ndiv, n // ndiv], ndiv + 1)
    return divisors_aux(n, divs, ndiv+1)


def divisors(n: int):
    """
    nの約数をリストで返す関数。ただし、0は空リストを返す。
    >>> divisors(0)
    []
    >>> divisors(10)
    [1, 2, 5, 10]
    如何ともしがたいn = 0, 1の時を例外にして処理。
    1まで別々で場合分けするの、ダサい。
    2以上は補助関数に丸投げ。
    """
    if n < 0:
        raise ValueError("値は正の数でなければなりません。")
    elif n == 0:
        return []
    elif n == 1:
        return [1]
    return divisors_aux(n, [1, n], 2)


def sum_of_divisors(n: int):
    """
    約数の和を返す関数。
    >>> sum_of_divisors(10)
    18
    >>> sum_of_divisors(1)
    1
    58で出たリストの和を求める。
    """
    return sum(divisors(n))


def divisors2(n: int):
    """
    nの約数をリストで返す関数。ただし、0は空リストを返す。
    >>> divisors(0)
    []
    >>> divisors(10)
    [1, 2, 5, 10]
    再帰処理がpythonの制限でイマイチ動かないので、おとなしくループで。
    """
    lst = []
    if n == 0:
        lst = []
    if n < 3:
        lst = [1, n]
    nnum = 2
    while True:
        nnum2 = nnum * nnum
        if nnum2 == n:
            lst.append(nnum)
            break
        if nnum2 > n:
            break
        if n % nnum == 0:
            lst += [nnum, n // nnum]
        nnum += 1
    return lst


# import sys
# sys.setrecursionlimit(2000)
# pythonのrecursionの上限が1000な関係で、most_divisors(1000)が動かない。
# recursionlimitの上限を2000に変えてあげる。許して。


def most_divisors(n: int, max=0, lst=[]):
    """
    nまでで最大の約数の個数となる数をリストで返す関数。
    >>> most_divisors(10)
    [6, 8, 10]
    >>> most_divisors(1)
    [1]
    その時のnの約数の長さを取得し、条件分け。
    """
    if n < 1:
        return lst
    nlen = len(divisors(n))
    if nlen > max:
        return most_divisors(n - 1, nlen, [n])
    if nlen == max:
        return most_divisors(n - 1, max, [n] + lst)
    return most_divisors(n - 1, max, lst)


def mul_lst(l: list):
    mul = 1
    for i in l:
        mul *= i
    return i


def lst_double(l1: list, l2: list):
    return [i for i in l1 if i in l2]


import math


def my_is_square(n: int):
    return math.sqrt(n).is_integer() 


def gcd2(x, y):
    """
    2数の最大公約数を返す関数。
    >>> gcd2(12, 15)
    3
    >>> gcd2(15, 7)
    1
    互除法を使わずにやりたいなって関数。
    4とか8とかを素因数にもつと違う答えを吐く。
    なんか思いついたら改善します。
    """
    if x == 0 or y == 0:
        return max2(x, y)
    return mul_lst(lst_double(divisors(x), divisors(y)))


def gcd3(x: int, y: int, z = 1):
    """
    3数の最大公約数を返す関数。
    >>> gcd3(3, 6, 9)
    3
    >>> gcd3(100, 200, 300)
    100
    zを入れなくても困らないように初期値1を設定。大は小を兼ねる。
    考え方はmax3()と一緒。
    """
    return gcd2(gcd2(x, y), z)

# import sys
# sys.setrecursionlimit(2000)
# pythonのrecursionの上限が1000な関係で、most_divisors(1000)が動かない。
# recursionlimitの上限を2000に変えてあげる。許して。


def gcd_all_aux(xs, gcd):
    """
    gcd_all()の補助関数。
    xsの要素をひとつづつ今の最大値と比べる。
    """
    if xs == []:
        return gcd
    return gcd_all_aux(xs[1:], gcd2(xs[0], gcd))


def gcd_all(xs: list):
    """
    リストxs内の全ての数を対象とした最大公約数を返す関数。
    >>> gcd_all([2, 4, 6])
    2
    >>> gcd_all([4, 8, 12, 16])
    4
    リストの要素が1個以下は例外として処理。
    後は補助関数に丸投げ。
    """
    if xs == []:
        raise ValueError("対象となる数が存在しません。")
    if len(xs) == 1:
        return xs[0]
    return gcd_all_aux(xs[1:], xs[0])


def is_perfect(n):
    """
    完全数かどうか判定する関数。
    >>> is_perfect(6)
    True
    >>> is_perfect(2)
    False
    定義通りか調べるだけ。
    """
    return sum_of_divisors(n) == 2 * n


def next_perfect(n: int):
    """
    nの次の完全数を求める関数。
    >>> next_perfect(6)
    28
    >>> next_perfect(5)
    6
    496の次の完全数がデカいので、おとなしく再帰じゃなくループでやる。
    """
    num = n + 1
    while True:
        if is_perfect(num):
            return num
        num += 1

import math
import numpy as np


def order_m(n):
    a = int(math.log(n) ** 2)
    for i in range(1, n):
        order = 0
        prod = 1
        for j in range(1, i):
            prod = prod * n % i
            if prod == 1:
                order = j
                break
        if order > a:
            return i
    return n


def my_primes(r):
    n = r
    res = {1, n}
    for p in range(2, int(math.sqrt(r)) + 1):
        while n % p == 0:
            res.add(p)
            n /= p
    return res


def tortient(r):
    ps = my_primes(r)
    res = r
    for p in ps:
        res = res * (p - 1) / p
        return res


class PolynomialModulo(object):

    def pow(self, ls, n, r):
        self.ls = ls
        self.n = n
        self.r = r
        return self.__pow(self.n)

    def __pow(self, m):
        if m == 1:
            return self.ls
        if m % 2 == 0:
            pls = self.__pow(m // 2)
            return self.__product(pls, pls)
        else:
            return self.__product(self.__pow(m - 1), self.__pow(1))

    def __product(self, ls1, ls2):
        res = [0] * min(len(ls1) + len(ls2) - 1, self.r)
        for i in range(len(ls1)):
            for j in range(len(ls2)):
                res[(i + j) % self.r] += ls1[i] * ls2[j]
        l = len(res)
        for k in reversed(range(l)):
            res[k] %= self.n
            if k == len(res) - 1 and res[k] == 0:
                res.pop(k)
        return res


def is_congruent(a, n, r):
    p = PolynomialModulo()
    i = n % r
    ls2 = [0] * (i + 1)
    ls2[0] = a % n
    ls2[i] = 1
    return p.pow([a, 1], n, r) == ls2


def is_prime2(n: int):
    """
    nが素数かどうか、AKS素数判定法を用いて解く関数。
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    https://ja.wikipedia.org/wiki/AKS%E7%B4%A0%E6%95%B0%E5%88%A4%E5%AE%9A%E6%B3%95
    5からは良く分からなかったので、インターネットから。
    今度ちゃんと勉強します。
    """
    if n < 1:
        raise ValueError("is_prime()", "2以上の自然数ではありません。", n)
    if n == 1:
        return False
    r = 1
    # 1.累乗数かどうか判定
    size = int(math.log2(n) + 1)
    for i in range(2, size):
        a = int(math.pow(n, 1 / i))
        if a ** i == n or (a + 1) ** i == n:
            return False
    # 2.or(n) > 4log^2(n)となるrを見つける。
    r = order_m(n)
    # 3.a < rの任意のaが1 < gcd(a,n) < nとなれば、nは合成数。
    for i in range(1, r + 1):
        if 1 < gcd2(i, n) < n:
            return False
    # 4.n <= rなら、nは素数。
    if n <= r:
        return True
    # 5. 剰余多項式の計算
    #    1 <= a <= [sqrt(phi(r))logn]の任意のaに対して、
    #    (X + a)^n != X^n + a (mod X^r - 1, n)ならば、nは合成数。
    #    ただし、phiはトーシェント関数。
    try:
        int(math.sqrt(tortient(r) * math.log(n)))
    except TypeError:
        print(n, r)
    for a in range(1, int(math.sqrt(tortient(r)) * math.log(n)) + 1):
        if not is_congruent(a, n, r):
            return False
    # 6. 素数。
    return True

# print(list(filter(is_prime, range(1, 30))))


def is_prime(n):
    """
    nが素数かどうか、判定する関数。
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    合成数と分かったらそこで探索を打ち切る。
    ただし、大きな数の素数は判定がとても遅い。
    O(n)がO(sqrt(n))になっただけなので...
    """
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes(n):
    """
    n以下の素数はいくつか？調べる関数。
    >>> primes(10)
    4
    >>> primes(1000)
    168
    nが素数なら1を、そうでないなら0を入れ、その和を返す。
    """
    return sum([1 if is_prime(i) else 0 for i in range(1, n+1)])

#fixme: 3000~4000の間に死ぬほど遅い数がある説。
#print(primes(10000))

def max_prime_under(n):
    """
    nを超えない最大の素数を返す関数。
    >>> max_prime_under(10)
    7
    >>> max_prime_under(100)
    97
    デカい方から調べて、素数だったらリターンしたほうが早い。
    ついでに、偶数は素数じゃないことは結構すぐ分かるので、2飛ばしにしちゃおうという算段。
    """
    n -= 1
    if is_even(n):
        n -= 1
    for i in range(n, 1, -2):
        if is_prime(i):
            return i


def submax_prime_under(n):
    """
    2回繰りかえせばゴールにたどり着くはず。
    """
    return max_prime_under(max_prime_under(n))


def sum_primes_under(n):
    """
    n未満の素数の和を返す。
    >>> sum_primes_under(10)
    17
    >>> sum_primes_under(100)
    1060
    結構なんでもいいかって感じで、2~nまで全探索。
    2ごとに飛ばすとか、いろいろやりようはあるはず。
    """
    return sum([i if is_prime(i) else 0 for i in range(2, n)])


# import sys
# sys.setrecursionlimit(15000)

def sum_primes_nth2(n: int, num=2, ret=0):
    """
    n番目までの素数和を返す。
    ただし、2個目の引数は補助用。
    基本的にこのような使い方をするべきではない。
    >>> sum_primes_nth(4)
    17
    >>> sum_primes_nth(5)
    28
    個数nが0になるまで、ループする。
    素数じゃないのが混じらないように、今の数をnで手伝ってあげる。
    """
    if n < 1:
        return ret
    if is_prime(num):
        return sum_primes_nth2(n-1, num+1, ret+num)
    return sum_primes_nth2(n, num+1, ret)
    

def sum_primes_nth(n):
    """
    n番目までの素数和を返す。
    >>> sum_primes_nth(4)
    17
    >>> sum_primes_nth(5)
    28
    個数が1個未満なら0,最初の素数として2を初期値にしておく。
    numが素数なら追加、そうではなければnumを2ずつ増やす。
    面白い解答、考え中。
    """
    if n < 1:
        return 0
    ret = 2
    num = 3
    for i in range(1, n):
        while True:
            if is_prime(num):
                print(num)
                ret += num
                num += 2
                break
            num += 2
    return ret


def factor_integer(n: int):
    """
    nを素因数分解する関数。
    >>> factor_integer(4)
    [2, 2]
    >>> factor_integer(2147483647)
    [2147483647]
    3以下なら、そのまま返す。
    nが素数になるまで、2割り、3割りをひたすらしていく。
    """
    if n < 4:
        return [n]
    num = 2
    ret = []
    while not is_prime(n):
        while n % num == 0:
            ret.append(num)
            n = n // num
        num += 1
        while not is_prime(num):
            num += 1
    ret.append(n)
    return ret


def times_n_rec(xs, n):
    """
    リスト各要素をn倍して返す。
    >>> times_n([1, 2, 3], 2)
    [2, 4, 6]
    >>> times_n(["a", "b"], 2)
    ["aa", "bb"]
    文字列も*演算子でいい感じにできるってことが出題意図かな？
    この辺で、リスト内包表現か、再帰が使えるとオシャレ。
    せっかくここまでやったんだから、色々使えるようになるといいね。
    """
    if xs == []:
        return []
    return [xs[0] * n] + times_n_rec(xs[1:], n)


def times_n_lst(xs: list, n: int):
    """
    リスト内包表現バージョン。
    きれいに収まる。
    """
    return [x * n for x in xs]


def times_n(xs: list, n: int):
    """
    ループバージョン。
    内包表現に比べて、煩わしくね？って感じ。
    せっかくpythonやるなら、内包表現で書けるようになりたい。
    """
    ret = []
    for i in xs:
        ret += [i * n]
    return ret


def even_index(xs: list):
    """
    リストの偶数要素を抜き出す。ただし、0番目も含む。
    >>> even_index([0, 1, 2])
    [0, 2]
    >>> even_index(["a", "b", "c"])
    ["a", "b"]
    74と同じノリ。
    """
    if xs == []:
        return []
    return [xs[0]] + even_index(xs[2:])


def evens_only(xs: list):
    """
    リストの偶数だけを取り出す。
    >>> evens_only([1, 2, 4, 3])
    [2, 4]
    >>> evens_only([1])
    []
    再帰で。74, 75と同じような感じ。
    """
    if xs == []:
        return []
    if is_even(xs[0]):
        return [xs[0]] + evens_only(xs[1:])
    return evens_only(xs[1:])


def repeat_item(item, m: int):
    """
    itemをm個詰めたリストを返す関数。
    >>> repeat_item(0, 3)
    [0, 0, 0]
    >>> repeat_item("abc", 2)
    ["abc", "abc"]
    一番普通の解き方。python君は賢いので、-1とか考慮しなくていいらしい。
    """
    return [item] * m


def repeat_item_lst(item, m: int):
    """
    リスト内包表現バージョン。
    for文のiがいらない時は_にすると、いい。
    """
    return [item for _ in range(0, m)]


def repeat_item_rec(item, m: int):
    """
    再帰バージョン。
    まあ、この問題では使わなくていいかな。
    """
    if m <= 0:
        return []
    return [item] + repeat_item_rec(item, m - 1) 


def zip_(xs: list, ys: list):
    """
    リストの要素をそれぞれzipする。
    ただし、必ずxsとysの個数は等しくする必要がある。
    >>> zip_([1, 3, 4], [1, 3, 5])
    [[1, 1], [3, 3], [4, 5]]
    >>> zip_([1], ["a"])
    [[1, "a"]]
    リストの要素数が違ったらエラーを返してもいいのだが、
    再帰するたびに呼ばれると面倒くさい。補助関数にするのもめんどくさいので、諦め。
    後は普通に再帰するだけ。
    """
    if xs == []:
        return []
    return [[xs[0], ys[0]]] + zip_(xs[1:], ys[1:])


def distinct(xs: list):
    """
    重複を除いて返す関数。ただし、順番は保証しない。
    >>> distinct([1,2,3,1])
    [1,2,3]
    >>> distinct([1,2,3])
    [1,2,3]
    セットで重複を解消、リストに戻す。
    """
    return list(set(xs))


def join_distinctly(xs: list, ys: list):
    """
    二つのリストから作った重複要素のないリストを返す関数。
    >>> distinct([1, 2], [1, 3])
    [1, 2, 3]
    >>> distinct([], [])
    []
    リストを演算子+で結合して、distinctに投げ込む。
    """
    return distinct(xs + ys)


def is_square(n: int):
    """
    全探索より二分探索で。
    この方法だとn = 0,1のときは判別不可。
    """
    if n < 2:
        return True
    min = 0
    max = n
    while min + 1 < max:
        avg = (min + max) // 2
        if avg * avg <= n:
            min = avg
        else:
            max = avg
    return min * min == n


def fibo(n: int):
    """
    定義通りにフィボナッチ数列を計算する関数。
    >>> fibo(2)
    1
    >>> fibo(4)
    3
    """
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


