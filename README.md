# FreeDom

## Paper
FREEDOM: Engineering a State-of-the-Art DOM Fuzzer (to appear) (ACM CSS 2020)

## Prerequisites
- Python 3.x

## Usage
```
python3 main.py
```

### Fuzzer configuration
Check `config.py` that manages testcase complexity and fuzzing process.

### Mode 0. Testcase generation only
This mode simply generates a number of random HTML documents and save them to a given directory.

Example:
```
python main.py -i 1 -m generate -n 10 -o output
```

## Security bugs

* WebKit (Safari): CVE-2019-6212, CVE-2019-8596, CVE-2019-8609, CVE-2019-8720, CVE-2020-9803, CVE-2020-9806, CVE-2020-9807, CVE-2020-9895
* Chrome: CVE-2019-5806, CVE-2019-5817, Issue 943424, Issue 943538
* Firefox: Issue 1626152

## Citation
```
@inproceedings{xu:freedom,
  title        = {{FREEDOM: Engineering a State-of-the-Art DOM Fuzzer (to appear)}},
  author       = {Wen Xu and Soyeon Park and Taesoo Kim},
  booktitle    = {Proceedings of the 27th ACM Conference on Computer and Communications Security (CCS)},
  month        = nov,
  year         = 2020,
  address      = {Orlando, FL},
}
```

## Contacts

* Wen Xu <wen.xu@gatech.edu>
* Soyeon Park <soyeon@gatech.edu>
* Taesoo Kim <taesoo@gatech.edu>
