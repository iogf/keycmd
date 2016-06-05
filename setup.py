from distutils.core import setup
setup(name="Keycmd",
      version="2.1.1",
      packages=["cmdlib", 'cmdlib.modes'],
      scripts=['keycmd'],
      package_data={'cmdlib': ['cmdrc', '/cmdrc/cmdrc']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br",
      url='https://github.com/iogf/keycmd',
      download_url='https://github.com/iogf/keycmd/releases',
      keywords=['vim', 'vy', 'keycmd', 'filemanager'],
      classifiers=[],
      description="A modal/Vim-like file manager. Keycmd is a very flexible file manager")


















