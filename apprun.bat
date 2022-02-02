@REM ミーティングID
set MEETINGID=
@REM ミーティングパスワード
set PASSWD=
@REM 授業時間（分）
set RECTIME=
@REM チャットメッセージ（出席確認用）
set MSG=

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5