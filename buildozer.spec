[app]
title = Rostelecom Travel
package.name = Rostelecom
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas ,json , mp4 , source/* 
source.include_patterns = sprite/*, dialog_window/*

version = 0.666

requirements = python3,kivy,kivymd ,sdl2_ttf, pillow , plyer , kivy-garden.mapview  , olefile , sdl2, sdl2_image, sdl2_mixer , pyjnius,pillow,requests,kivy-garden.mapview 

orientation = portrait
fullscreen = 1


android.api = 32
android.minapi = 21
android.arch = arm64-v8a,armeabi-v7a


icon.filename = 1.jpg
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE , INTERNET

[buildozer]
log_level = 2