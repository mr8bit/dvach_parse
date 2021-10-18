import argparse
import json
import logging
import pathlib
import time

import api2ch
from tqdm.contrib.concurrent import process_map

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Парсинг бордов с двача.')
parser.add_argument('--boards', dest='boards', type=str, help='Cписок бордов для парсинга --board=b,2ch')
parser.add_argument('--save_dir', type=str, help='Путь для сохранения постов --save_dir="./saved_dir"')
parser.add_argument('--max_workers', type=int, default=6,
                    help='Количество воркеров для одновременного скачивания тредов --save_dir="./saved_dir"')

args = parser.parse_args()
if args.boards:
    print(args.boards.split(','))

api = api2ch.Api2ch()
boards = []
if not args.boards:
    logger.info(f"Парсим все доски с Двача")
    for board in api.boards().boards:
        boards.append(board.id)
else:
    logger.info(f"Парсим с выбранных досок: {args.boards}")
    boards = args.boards.split(',')

p = pathlib.Path(args.save_dir)
p.mkdir(parents=True, exist_ok=True)


def download_from_board(board):
    try:
        time.sleep(0.45)
        p = pathlib.Path(f"{args.save_dir}/{board}")
        p.mkdir(parents=True, exist_ok=True)
        threads = api.threads(board).threads
        for thread in threads:
            fn = f"{thread.num}.json"
            filepath = p / fn
            posts = api.thread_posts_by_num(board, thread.num, num=thread.num)
            saved = posts.dict()
            saved.pop('request', None)
            with filepath.open("w", encoding="utf-8") as f:
                json.dump(saved, f)
    except Exception as e:
        print(e)


data = process_map(download_from_board, boards, max_workers=args.boards, chunksize=3)
