from pywinauto import Application
import pywinauto

import time

def captureZoom():
    while True:
        try:
            # パスコード入力ウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"ミーティング パスコードを入力")
            break
        except pywinauto.findbestmatch.MatchError: #  -> 再取得
            continue

    zoom[u"ミーティング パスコードを入力"].set_focus() # パスコード入力ウィンドウ
    pywinauto.keyboard.send_keys("c6cVBV") # パスワード入力
    pywinauto.keyboard.send_keys("{ENTER}") # Enter（入室）
    
    time.sleep(5)
    
    while True:
        try:
            pywinauto.keyboard.send_keys("%{VK_MENU down}%{H down}%{VK_MENU up}%{H up}") # チャットウィンドウ起動
            # チャットウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"チャット")
            zoom[u"チャット"].set_focus()
            break
        except pywinauto.findbestmatch.MatchError: #  -> 再取得
            continue
    pywinauto.keyboard.send_keys("80538IH13A115金子凌大") # 出席入力
    pywinauto.keyboard.send_keys("{ENTER}") # チャット送信
    pywinauto.keyboard.send_keys("{ESC}") # チャットウィンドウ閉じる
    
    while True:
        try:
            # Zoomミーティングウィンドウ情報取得
            zoom = Application(backend="uia").connect(best_match=u"Zoom ミーティング")
            zoom[u"Zoom ミーティング"].set_focus() # 録画対象
            break
        except pywinauto.findbestmatch.MatchError: # Zoomミーティング入室していない -> 再取得
            continue
    
    pywinauto.keyboard.send_keys("{VK_LWIN down}%{R down}{VK_LWIN up}{R up}") # 録画開始
    
    time.sleep(30)
    # time.sleep(5400) # 90分
    
    pywinauto.keyboard.send_keys("%{VK_MENU down}%{H down}%{VK_MENU up}%{H up}") # チャットウィンドウ起動
    pywinauto.keyboard.send_keys("80538IH13A115金子凌大") # 出席入力
    pywinauto.keyboard.send_keys("{ENTER}") # チャット送信
    pywinauto.keyboard.send_keys("{ESC}") # チャットウィンドウ閉じる
    pywinauto.keyboard.send_keys("{VK_LWIN down}%{R down}{VK_LWIN up}{R up}") # 録画終了

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