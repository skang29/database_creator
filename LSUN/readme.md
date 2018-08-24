# LSUN, Large-Scale Scene Understanding Database
## Dataset information
| Category | Training | Validation |
| :--:| :--: | :--: |
| Bedroom	| 3,033,042 images (43 GB) | 300 images | 
| Bridge	| 818,687 images (16 GB)	| 300 images| 
| Church Outdoor	| 126,227 images (2.3 GB)	| 300 images| 
| Classroom	| 168,103 images (3.1 GB)	| 300 images| 
| Conference Room	| 229,069 images (3.8 GB)	| 300 images| 
| Dining Room	| 657,571 images (11 GB)	| 300 images| 
| Kitchen	| 2,212,277 images (34 GB)	| 300 images| 
| Living Room	| 1,315,802 images (22 GB)	| 300 images| 
| Restaurant	| 626,331 images (13 GB)	| 300 images| 
| Tower	| 708,264 images (12 GB)	| 300 images| 
| Testing Set	| 10,000 images (173 MB)| 

## Download dataset
This instruction is for Windows 10 user using WSL to download LSUN dataset. 

Original LSUN Dataset documentation and demo codes are here: [GitHub](https://github.com/fyu/lsun)

Please make sure you have cURL installed
```bash
# Download the whole latest data set
python2.7 download.py
# Download the whole latest data set to <data_dir>
python2.7 download.py -o <data_dir>
# Download data for bedroom
python2.7 download.py -c bedroom
# Download testing set
python2.7 download.py -c test
```

## Extract dataset
Downloaded file includes lmdb file. To extract the file, you need to install lmdb library.

```bash
pip install lmdb
```

If you experience **UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb8 in position 5: invalid start byte** error, change **{YOUR_PYTHON_PATH}/lib/site-packages/pip/compat/__init__.py** file as shown below.

```bash
# Python 3.6
return s.decode('utf-8')

to

return s.decode('cp949')
```

This is not permanenet solution for the error. However, it works!

You can use original author's extraction code, however, for version compatibility, I created **lmdb_extractor.py** based on original code.

For example, when you want to extract bridge_train_lmdb use this code.
```bash
# Python 3.6
python lmdb_extractor.py ./bridge_train_lmdb --out_dir=./bridge_train_image --flat
```

## Crop image for me.
```bash
# Python 3.6
python create_database.py --result_size 256 -d ../LSUN_BRIDGE_CENTER_SQUARE_256/data.npy -p F:/Databases/LSUN/bridge_train_image -s --nonpy
```
