@REM �~�[�e�B���OID
set MEETINGID=
@REM �~�[�e�B���O�p�X���[�h
set PASSWD=
@REM ���Ǝ��ԁi���j
set RECTIME=
@REM �`���b�g���b�Z�[�W�i�o�Ȋm�F�p�j
set MSG=

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5