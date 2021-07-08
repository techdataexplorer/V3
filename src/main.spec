# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Windows\\System32\\downlevel', 'C:\\Users\\techs\\tdx_desktop_deploy\\github_source\\V3\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


 a.datas += [('SD_logo.png', './img/SD_logo.png', 'DATA'),
             ('sd-icon.png', './img/sd-icon.png', 'DATA'),
             ('plus-icon.png', './img/plus-icon.png', 'DATA'),
             ('placeholder.png', './img/placeholder.png', 'DATA'),
             ('folder-icon.png', './img/folder-icon.png', 'DATA'),
             ('user.png', './img/user.png', 'DATA'),
             ('mapView.html', './mapView.html', 'DATA')
            ]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
