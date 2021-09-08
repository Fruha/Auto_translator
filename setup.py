from distutils.core import setup
setup(
  name = 'FruxaAT',         # How you named your package folder (MyLib)
  packages = ['FruxaAT'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='ISC',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library could be useful students who are not good in English',   # Give a short description about your library
  author = 'Fruxa',                   # Type in your name
  author_email = 'fruha1980@mail.ru',      # Type in your E-Mail
  url = 'https://github.com/Fruha/Auto_translator',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Fruha/Auto_translator/archive/refs/tags/v_0.1.tar.gz',    # I explain this later on
  keywords = ['English', 'translate', 'vk', 'cheating'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
            "pytesseract",
            "opencv-python",
            "googletrans==3.1.0a0",
            "plyer",
            "pyautogui",
            "pynput",
            "keyboard",
            "vk_api",
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: ISC License',   # Again, pick a license
    'Programming Language :: Python :: 3.8',
  ],
)