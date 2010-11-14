from distutils.core import setup
import sys

sys.path.append("vt102")
import vt102

setup(name="vt102",
      version="0.1",
      author="Sam Gibson",
      author_email="sam@ifdown.net",
      url="https://github.com/samfoo/vt102",
      description="Simple vt102 emulator, useful for screen scraping.",
      long_description=vt102.__doc__,
      package_dir={"": "vt102"},
      py_modules=["vt102"],
      provides=["vt102"],
      keywords="vt102 terminal emulator screen scraper",
      license="Lesser General Public License v3.0",
)