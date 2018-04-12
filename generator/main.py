import argparse
from datetime import datetime
import logging
import time
import os
import sys

from utils import dbpediacleaner, fbcleaner, rdfcleaner

DEFAULT_LOG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               'log/{}'.format(datetime.now().strftime('%Y%m%d_%H:%M')))
logger = logging.getLogger()

if __name__ == '__main__':
    p = argparse.ArgumentParser('Dataset Generator')
    p.add_argument('--graph', type=str, help='path of knowledge graph')
    p.add_argument('--outpath', type=str, help='output path for the dataset')
    p.add_argument('--cleaner', type=str, help='[dbpedia, fb, yago]')
    p.add_argument('--ent_th', type=float, help='threshold for filtering long-tail entity')
    p.add_argument('--rel_th', type=int, help='threshold for filtering long-tail relation')
    p.add_argument('--test_size', default=1000, type=int, help='the size of test dataset')
    p.add_argument('--valid_size', default=1000, type=int, help='the size of validation dataset')

    # others
    p.add_argument('--log', default=DEFAULT_LOG_DIR, type=str, help='output log dir')

    args = p.parse_args()

    # setting for logging
    if not os.path.exists(args.log):
        os.mkdir(args.log)
    # logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    log_path = os.path.join(args.log, 'log')
    file_handler = logging.FileHandler(log_path)
    fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    logger.info('begin to load graph')
    load_start = time.time()

    if args.cleaner == "dbpedia": 
        g = dbpediacleaner.DBPediaCleaner(args).run()
    elif args.cleaner == "fb":
        g = fbcleaner.FBCleaner(args).run()
    elif args.cleaner == "yago":
        g = yagocleaner.YagoCleaner(args).run()
    elif args.cleaner == "dbpedia_dict":
        dbpediacleaner.DBPediaCleaner(args).generate_rdf_dict()
    elif args.cleaner == "fb_dict":
        dbpediacleaner.FBCleaner(args).generate_rdf_dict()
    elif args.cleaner == "yago_dict":
        dbpediacleaner.YagoCleaner(args).generate_rdf_dict()

    logger.info('graph loading time in {} seconds'.format(time.time() - load_start))
