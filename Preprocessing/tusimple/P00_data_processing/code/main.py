import os

from options.config import Config
from options.args import *
from libs.preprocess import *

def run(cfg, dict_DB):
    preprocessor = Preprocessing(cfg, dict_DB)
    preprocessor.run()

#  python main.py --dataset_dir /home/autolabelling/datasets/tusimple/TUSimple/
def main():
    # option
    cfg = Config()
    cfg = parse_args(cfg)

    # prepare
    dict_DB = dict()

    # run
    run(cfg, dict_DB)

if __name__ == '__main__':
    main()
