@REM �~�[�e�B���OID
set MEETINGID=71573572426
@REM �~�[�e�B���O�p�X���[�h
set PASSWD=zM44Z5
@REM ���Ǝ��ԁi���j
set RECTIME=1
@REM �`���b�g���b�Z�[�W�i�o�Ȋm�F�p�j
set MSG=80538IH13A115���q����

start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%
python ./app.py %PASSWD% %RECTIME% %MSG%
timeout /t 5