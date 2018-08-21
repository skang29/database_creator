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

### Demo code

#### Dependency

Install Python

Install Python dependency: numpy, lmdb, opencv

#### Usage:

View the lmdb content

```bash
python2.7 data.py view <image db path>
```

Export the images to a folder

```bash
python2.7 data.py export <image db path> --out_dir <output directory>
```

#### Example:

Export all the images in valuation sets in the current folder to a
"data"
subfolder.

```bash
python2.7 data.py export *_val_lmdb --out_dir data

