from .voice import Speaker, get_speaker_info
import traceback
import sys


def zundamon_says(args: str):
    error_txt = ''.join(args)
    print(error_txt)
    Speaker(get_speaker_info().name['ずんだもん']['ノーマル'],
            enable_cache=True).text(error_txt).speak()
    return error_txt


def _exception_hook(cls, er, tb):
    if cls is FileNotFoundError:
        zundamon_says(
            f'{er.filename}というファイルやフォルダはないのだ。'
        )
    elif cls is FileExistsError:
        zundamon_says(
            f'{er.filename}というファイルやフォルダが既にあるのだ。'
        )
    elif cls is IsADirectoryError:
        zundamon_says(f'{er.filename}はディレクトリなのだ。')
    elif cls is NotADirectoryError:
        zundamon_says(
            f'{er.filename}はディレクトリではないのだ。'
        )
    elif cls is PermissionError:
        zundamon_says(
            f'{er.filename}に対して十分なアクセス権がないのだ。'
        )
    elif cls is ProcessLookupError:
        zundamon_says('プロセスが見付からないのだ。')
    elif cls is TimeoutError:
        zundamon_says('タイムアウトなのだ。')
    elif cls is InterruptedError:
        zundamon_says('中断するように言われたのだ。')
    elif cls is ConnectionRefusedError:
        zundamon_says('接続が拒否されたのだ。')
    elif cls is ConnectionAbortedError:
        zundamon_says('接続が中断されたのだ。')
    elif cls is BrokenPipeError:
        zundamon_says('パイプが壊れたのだ。')
    elif cls is ChildProcessError:
        zundamon_says('子プロセスが失敗したのだ。')
    elif cls is BlockingIOError:
        zundamon_says('非同期処理に失敗したのだ。')
    elif cls is UnicodeEncodeError:
        zundamon_says('ユニコードのエンコードに失敗したのだ。')
    elif cls is UnicodeDecodeError:
        zundamon_says('ユニコードのデコードに失敗したのだ。')
    elif cls is UnboundLocalError:
        zundamon_says('ローカル変数が変なのだ。')
    elif cls is TypeError:
        zundamon_says('型のエラーなのだ。')
    elif cls is NameError:
        zundamon_says(f'{er.name}は定義されていないのだ。')
    elif cls is ZeroDivisionError:
        zundamon_says('ゼロで割り算をしてはいけないのだ。')
    elif cls is OverflowError:
        zundamon_says('オーバーフローなのだ。')
    elif cls is ArithmeticError:
        zundamon_says('数学的に間違いなのだ。')
    elif cls is AssertionError:
        zundamon_says('テストが失敗したようなのだ。')
    elif cls is AttributeError:
        zundamon_says('属性のエラーなのだ。')
    elif cls is EOFError:
        zundamon_says('文字が入力されなかったのだ。')
    elif cls is ImportError:
        zundamon_says(f'{er.name}をインポートできなかったのだ。')
    elif cls is ModuleNotFoundError:
        zundamon_says(f'{er.name}をインポートできなかったのだ。')
    elif cls is IndexError:
        zundamon_says('添字が範囲外なのだ。')
    elif cls is KeyError:
        zundamon_says('辞書のキーが違うのだ。')
    elif cls is KeyboardInterrupt:
        zundamon_says(
            'ユーザーさんが中止しろって言ったからやめたのだ。'
        )
    elif cls is MemoryError:
        zundamon_says('メモリー不足なのだ。')
    elif cls is BufferError:
        zundamon_says('バッファ関連のエラーなのだ。')
    elif cls is LookupError:
        zundamon_says('キーが違うのだ。')
    elif cls is OSError:
        zundamon_says('OS関連のエラーなのだ。')
    elif cls is RecursionError:
        zundamon_says('無限ループしていそうなのだ。')
    elif cls is ReferenceError:
        zundamon_says('既にガベコレされているのだ。')
    elif cls is RuntimeError:
        zundamon_says('何かよくわからないエラーなのだ。')
    elif cls is IndentationError:
        zundamon_says('インデントがおかしいのだ。')
    elif cls is TabError:
        zundamon_says('タブとスペースどっちかにすべきなのだ。')
    elif cls is SystemError:
        zundamon_says('インタプリタのエラーなのだ。')
    elif cls is SyntaxError:
        zundamon_says('文法が間違っているのだ。')
    elif isinstance(er, ZundamonSays):
        pass
    else:
        zundamon_says('何らかのエラーなのだ。')
    traceback.print_exception(cls, er, tb)


sys.excepthook = _exception_hook


class ZundamonSays:
    def __str__(self):
        error_txt = ''.join(self.args)
        info = get_speaker_info().name['ずんだもん']['ノーマル']
        Speaker(info, enable_cache=True).text(error_txt).speak()
        return error_txt
