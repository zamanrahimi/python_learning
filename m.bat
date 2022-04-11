git add . 
@echo off

set /A c+=1
set /p id="Enter message: "
git commit -m "%c%"," - ","%id%"
git push 

