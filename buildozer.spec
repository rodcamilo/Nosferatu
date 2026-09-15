[app]
title = Nosferatu
package.name = nosferatu
package.domain = org.nosferatu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Icone do aplicativo (aponta para o arquivo icon.png na raiz)
icon.filename = %(source.dir)s/icon.png

# Fixando versoes estaveis do Android SDK/Build-Tools
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
p4a.branch = release-2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1