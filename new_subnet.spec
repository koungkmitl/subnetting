# -*- mode: python -*-
a = Analysis(['src/new_subnet.py'],
             pathex=['C:\\Python27\\Libs\\site-packages'],
             hiddenimports=['netaddr'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='new_subnet.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
