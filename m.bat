git add . 
@echo off
set /p id="Enter message: "
git commit -m "%id%"
git push 

