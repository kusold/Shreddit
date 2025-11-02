# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['shreddit/app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('shreddit/*.example', 'shreddit'),
    ],
    hiddenimports=[
        'pkg_resources.py2_warn',
        'appdirs',
        'yaml',
        'praw',
        'arrow',
        'tornado',
        'prometheus_client',
        'requests',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='shreddit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
