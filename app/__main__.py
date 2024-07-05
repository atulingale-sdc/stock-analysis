import sys
from os.path import abspath, join

sys.path.insert(0, abspath(join(__file__, "../", "../")))
sys.path.insert(0, abspath(join(__file__, "../")))

from app.bootstrap import boot


if __name__ == "__main__":
    cli = boot()
    cli()
