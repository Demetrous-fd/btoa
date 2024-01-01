
### Install
```shell
pip install btoa
```

### Example
```python
from btoa import btoa, atob

assert btoa("Hello World!") == "SGVsbG8gV29ybGQh"
assert atob("SGVsbG8gV29ybGQh") == "Hello World!"
```
