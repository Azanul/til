# Pydantic
-------------------------------------------

[Pydantic](https://docs.pydantic.dev) validates and converts convertable values to corrent data type and raise error if not convertable, using given type hints. 

**IMP**: [config](https://docs.pydantic.dev/usage/model_config/)

## Example with validator

```python
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, validator



class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime]
    friends: List[int] = []

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

class Book(BaseModel):
    title: str
    author: User


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)
book = Book(author=external_data, title="MyBook")

print(user)
print(book)
```

output:
```bash
id=123 signup_ts=datetime.datetime(2019, 6, 1, 12, 22) friends=[1, 2, 3] name='John Doe'
title='MyBook' author=User(id=123, signup_ts=datetime.datetime(2019, 6, 1, 12, 22), friends=[1, 2, 3], name='John Doe')
```


libraries like [camel-converter](https://pypi.org/project/camel-converter/) (use pydantic internally) can be used to fix naming convention too. Like changing
```json
{
  "Key": "Value"
  "MyKey": "MyValue"
}
```
to
```json
{
  "key": "Value"
  "my_key": "MyValue"
}
```
and vice-versa.
