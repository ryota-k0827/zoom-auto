from pywinauto import Application
import pywinauto

import time
import sys

passwd = sys.argv[1]
rec_time = sys.argv[2]
chat_msg = sys.argv[3]

def captureZoom():
    print("Zoom起動中...")
    while True:
        try:
            # パスコード入力ウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"ミーティング パスコードを入力")
            print("ミーティング パスコードを入力します")
            break
        except pywinauto.findbestmatch.MatchError: #  -> 再取得
            continue

    zoom[u"ミーティング パスコードを入力"].set_focus() # パスコード入力ウィンドウ
    pywinauto.keyboard.send_keys(passwd) # パスワード入力
    pywinauto.keyboard.send_keys("{ENTER}") # Enter（入室）
        
    print("ミーティングの開始を待機中...")
    while True:
        try:
            pywinauto.keyboard.send_keys("%{VK_MENU down}%{H down}%{VK_MENU up}%{H up}") # チャットウィンドウ起動
            # チャットウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"チャット")
            print("授業開始チャットを入力します")
            break
        except pywinauto.findbestmatch.MatchError: #  -> 再取得
            continue
    zoom[u"チャット"].set_focus()
    pywinauto.keyboard.send_keys(chat_msg) # 出席入力
    pywinauto.keyboard.send_keys("{ENTER}") # チャット送信
    pywinauto.keyboard.send_keys("{ESC}") # チャットウィンドウ閉じる
        
    while True:
        try:
            # Zoomミーティングウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"Zoom ミーティング")
            print("画面収録を開始します")
            break
        except: # Zoomミーティング入室していない -> 再取得
            continue
    zoom[u"Zoom ミーティング"].set_focus() # 録画対象
    time.sleep(1)
    pywinauto.keyboard.send_keys("{VK_LWIN down}%{VK_MENU down}%{R down}{VK_LWIN up}%{VK_MENU up}%{R up}") # 録画開始
    
    print("授業開始。"+rec_time+"分後に授業終了処理を開始します。")
    
    time.sleep(int(rec_time)*60) # 授業実施時間
    

    print("授業終了時間になりました。チャットを入力して退出します。")
    zoom[u"Zoom ミーティング"].set_focus()
    pywinauto.keyboard.send_keys("%{VK_MENU down}%{H down}%{VK_MENU up}%{H up}") # チャットウィンドウ起動
    pywinauto.keyboard.send_keys(chat_msg) # 出席入力
    pywinauto.keyboard.send_keys("{ENTER}") # チャット送信
    pywinauto.keyboard.send_keys("{ESC}") # チャットウィンドウ閉じる
    pywinauto.keyboard.send_keys("{VK_LWIN down}%{VK_MENU down}%{R down}{VK_LWIN up}%{VK_MENU up}%{R up}") # 録画終了

    # Zoom Client閉じる
    zoom = Application(backend="uia").connect(best_match=u"Zoom ミーティング")
    if zoom[u"Zoom ミーティング"].exists():
        zoom[u"Zoom ミーティング"].set_focus()
        pywinauto.keyboard.send_keys("%{F4}")
        pywinauto.keyboard.send_keys("{ENTER}")

def main():
    try:
        captureZoom()
    except pywinauto.findbestmatch.MatchError: # ターゲットが見つからなかった -> 再試行
        print("The dialog was not found. Retrying...")
        main()
    except pywinauto.findwindows.ElementNotFoundError: # ターゲットが見つからなかった -> 再試行
        print("The dialog was not found. Retrying...")
        main()

if __name__ == '__main__':
    main()