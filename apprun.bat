@REM ミーティングID
set MEETINGID=1234567890
@REM ミーティングパスワード
set PASSWD=password
@REM 授業時間（分）
set RECTIME=90
@REM チャットメッセージ（出席確認用）
set MSG=99999IH99A999山田太郎

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5