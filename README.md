ninvoicevoxにずんだエラーの機能を統合しました。
それに伴い、このリポジトリは古くなりました。
下記をお使い下さい。

https://github.com/uesseu/ninvoicevox


# ZundamonError
ずんだもんにpythonのエラーを報告させるものです。
単にVOICEVOXをpythonからキックしているだけです。
linuxの場合はaplayを音声の出力に使います。
ほとんど自分用なのでMACでどう動かすかは知りません。
教えてくれたらその限りではないけれど。

# インストール
```sh
pip install git+https://github.com/uesseu/zundaerror
```

# 使い方
VOICEVOXのサーバーを立てます。VOICEVOXはVOICEVOX ENGINEを使うといいです。
コマンドは当然pathに依存します。
ホームディレクトリにGPU依存のVOICEVOXを入れているならこうですね。

```sh
/home/hoge/voicevox/linux-nvidia/run
```

そんで、pythonのコードの中でzundaerrorをインポートします。

```python
import zundaerror
```

以上です。

# カスタムException
Exceptionをカスタマイズしたいなら```zundaerror.ZundamonSays```を継承します。

```python
import zundaerror

class ZundamonException(zundaerror.ZundamonSays, Exception):
    pass

raise ZundamonException('ずんだもんがエラーを報告するのだ。')
```

多重継承するので、ZundamonSaysの方が先です。

# TODO
四国めたんとかにも対応できたらいいな。
