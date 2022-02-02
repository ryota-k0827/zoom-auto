@REM ミーティングID
set MEETINGID=71573572426
@REM ミーティングパスワード
set PASSWD=zM44Z5
@REM 授業時間（分）
set RECTIME=1
@REM チャットメッセージ（出席確認用）
set MSG=80538IH13A115金子凌大

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5