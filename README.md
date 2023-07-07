Genit Library<a name="TOP"></a>
===================
[![Downloads](https://static.pepy.tech/personalized-badge/genit?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)](https://pepy.tech/project/genit)
![PyPI](https://img.shields.io/pypi/v/genit)

## Install Genit ##
```bash
pip install genit
```
## How it Works ? ##

### 1 -  Random String ###

The Gstr function use "abcdefghijklmnopqrstuvwxyz"

You can aslo add your own characters form add_characters parameter

```python

import genit

# 10 = length of generation
# "" = If you want to use your own characters like "$^&@!*-+±§"

random_string = genit.str(10, "")
print(random_string)

# output "opemauivye"
```

### 2 -  Random Integer ###

the Gint function use "1234567890"

```python
import genit

# 15 = length of generation

random_integer = genit.int(15)
print(random_integer)

# output "483226821395342"
```

### 3 -  Random All ###

The Gall function use "abcdefghijklmnopqrstuvwxyz1234567890"

You can aslo add your own characters form add_characters parameter

```python
import genit

# 8 = length of generation
# "" = If you want to use your own characters like "$^&@!*-+±§"

random_all = genit.all(8, "")
print(random_all)

# output "kf1a8s46"
```

### 4 -  Random Special ###

The Gspecial function use your own characters

```python
import genit

# 8 = length of generation
# "abc" = your own characters

random_special = genit.special(8, "abc")
print(random_special)

# output "abcccbab"
```
