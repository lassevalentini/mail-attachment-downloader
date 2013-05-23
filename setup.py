from distutils.core import setup
import py2exe

import compileall
compileall.compile_dir(".")

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob('C:\Windows\winsxs\Manifests\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.21022.8_none_bcb86ed6ac711f91.manifest')),
("Microsoft.VC90.CRT", glob('C:\Python27\DLLs\*.dll'))]
#setup(windows=[{"script" : "main.py"}], options={"py2exe" : {"includes" : ["sip","unicodecsv"]}})
setup(
    data_files=data_files,
    windows=[{"script" : "main.py",
            "icon_resources": [(1, "images/logo.ico")]}],
    options={"py2exe" : {
        "includes" : ["sip"],
        "packages": ['encodings']}})
