@echo off
setlocal enabledelayedexpansion
set ffmpeg2="C:\Program Files (x86)\YouKu\nplayer\ffmpeg.exe"
if exist %ffmpeg2% (
	for /r . %%i in (*.kux) do (
		%ffmpeg2% -y -i "%%i" -c:a copy -c:v copy -threads 2 "%%~dpni.mp4"
	)
) else echo

