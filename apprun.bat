@REM ミーティングID
set MEETINGID=
@REM ミーティングパスワード
set PASSWD=
@REM 授業時間（録画時間）
set RECTIME=90
@REM チャットメッセージ（出席確認用）
set MSG=80538IH13A115金子凌大

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 10