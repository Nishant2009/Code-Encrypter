# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/nisha/Desktop/Project Sem 3  updated/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/nisha/Desktop/Project Sem 3  updated/icon.ico', '.'), ('C:/Users/nisha/Desktop/Project Sem 3  updated/menu-button.png', '.'), ('C:/Users/nisha/Desktop/Project Sem 3  updated/ui_main.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Code Encryptor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\nisha\\Desktop\\Project Sem 3  updated\\icon.ico'],
)
