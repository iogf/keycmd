from distutils.core import setup
setup(name="Keycmd",
      version="2.0.0",
      packages=["cmdlib", 'cmdlib.modes'],
      scripts=['keycmd'],
      package_data={'cmdlib': ['cmdrc', '/cmdrc/cmdrc']},
      author="Iury O. G. Figueiredo",
      author_email="ioliveira@id.uff.br")












