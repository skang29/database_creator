from os.path import exists, join
import lmdb
import os

import argparse


def export_images(db_path, out_dir, flat=False, limit=-1):
    print('Exporting', db_path, 'to', out_dir)
    env = lmdb.open(db_path, map_size=1099511627776,
                    max_readers=100, readonly=True)
    count = 0
    with env.begin(write=False) as txn:
        cursor = txn.cursor()
        for key, val in cursor:
            key = key.decode('utf-8')
            # val = val.decode('utf-8')
            if not flat:
                image_out_dir = join(out_dir, '/'.join(key[:6]))
            else:
                image_out_dir = out_dir
            if not exists(image_out_dir):
                os.makedirs(image_out_dir)
            image_out_path = join(image_out_dir, key + '.webp')
            with open(image_out_path, 'wb') as fp:
                fp.write(val)
            count += 1
            if count == limit:
                break
            if count % 1000 == 0:
                print('Finished', count, 'images')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('lmdb_path', type=str,
                        help='The path to the lmdb database folder. '
                             'Support multiple database paths.')
    parser.add_argument('--out_dir', type=str, default='')
    parser.add_argument('--flat', action='store_true',
                        help='If enabled, the images are imported into output '
                             'directory directly instead of hierarchical '
                             'directories.')

    args = parser.parse_args()
    lmdb_path = args.lmdb_path

    export_images(lmdb_path, args.out_dir, args.flat)


if __name__ == '__main__':
    main()