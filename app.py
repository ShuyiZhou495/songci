## music player reference: https://github.com/Zegendary/Garbage/tree/master/%E5%A4%A7%E8%AE%BE%E8%AE%A1/simple%20music%20player/Random%20music%20player

from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from create_mid import create_midi, get_lyric_time
from fun_get_img import get_img

app = Flask(__name__)
bootstrap = Bootstrap(app)
fa = FontAwesome(app)

input = [{'lyrics': '還 愛 著 你 你 卻 把 別 人 擁 在 懷 裡', 'key': ['77', '77', '77', '80', '77', '77', '77', '77', '77', '76', '74', '72', '74'],'duration': ['0.2', '0.2', '0.2', '0.4', '0.7', '0.7', '1.3', '0.2', '0.2', '0.2', '0.2', '0.2', '0.4']}, {'lyrics': '不 能 再 這 樣 下 去', 'key': ['67', '74', '72', '69', '69', '67', '72'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '穿 過 愛 的 暴 風 雨', 'key': ['68', '63', '63', '65,68', '67', '72', '63'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '寧 願 清 醒 忍 痛 地 放 棄 你', 'key': ['65', '67', '69', '69', '67', '67', '65', '65', '67', '65'],'duration': ['0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3']}, {'lyrics': '還 愛 著 你 你 卻 把 別 人 擁 在 懷 裡', 'key': ['77', '77', '77', '80', '77', '77', '77', '77', '77', '76', '74', '72', '74'],'duration': ['0.2', '0.2', '0.2', '0.4', '0.7', '0.7', '1.3', '0.2', '0.2', '0.2', '0.2', '0.2', '0.4']}, {'lyrics': '不 能 再 這 樣 下 去', 'key': ['67', '74', '72', '69', '69', '67', '72'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '穿 過 愛 的 暴 風 雨', 'key': ['68', '63', '63', '65,68', '67', '72', '63'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '寧 願 清 醒 忍 痛 地 放 棄 你', 'key': ['65', '67', '69', '69', '67', '67', '65', '65', '67', '65'],'duration': ['0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3']}, {'lyrics': '還 愛 著 你 你 卻 把 別 人 擁 在 懷 裡', 'key': ['77', '77', '77', '80', '77', '77', '77', '77', '77', '76', '74', '72', '74'],'duration': ['0.2', '0.2', '0.2', '0.4', '0.7', '0.7', '1.3', '0.2', '0.2', '0.2', '0.2', '0.2', '0.4']}, {'lyrics': '不 能 再 這 樣 下 去', 'key': ['67', '74', '72', '69', '69', '67', '72'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '穿 過 愛 的 暴 風 雨', 'key': ['68', '63', '63', '65,68', '67', '72', '63'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '寧 願 清 醒 忍 痛 地 放 棄 你', 'key': ['65', '67', '69', '69', '67', '67', '65', '65', '67', '65'],'duration': ['0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3']}, {'lyrics': '還 愛 著 你 你 卻 把 別 人 擁 在 懷 裡', 'key': ['77', '77', '77', '80', '77', '77', '77', '77', '77', '76', '74', '72', '74'],'duration': ['0.2', '0.2', '0.2', '0.4', '0.7', '0.7', '1.3', '0.2', '0.2', '0.2', '0.2', '0.2', '0.4']}, {'lyrics': '不 能 再 這 樣 下 去', 'key': ['67', '74', '72', '69', '69', '67', '72'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '穿 過 愛 的 暴 風 雨', 'key': ['68', '63', '63', '65,68', '67', '72', '63'],'duration': ['0.2', '0.2', '0.2', '0.2', '0.2', '0.2', '0.2']},{'lyrics': '寧 願 清 醒 忍 痛 地 放 棄 你', 'key': ['65', '67', '69', '69', '67', '67', '65', '65', '67', '65'],'duration': ['0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3', '0.3']}]


def get_song(lyrics):
    """
    :param lyrics:
    :return the json file of generated song including duration and key and lyrics:
    """
    pass

@app.route('/to_song')
def to_song():
    lyrics = request.args.get('lyric')
    input_json = get_song(lyrics)
    music_path = create_midi(input)
    img_path = get_img(input)
    time_lyric = get_lyric_time(input)
    return render_template('2song.html',
                           music_path="static/upload/music/" + music_path,
                           lyric=lyrics,
                           img_path='static/upload/img/' + img_path,
                           time_lyric=time_lyric)

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run()
