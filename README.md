# Hashnode

This is a wrapper around the hashnode GraphQL API using python.

docs : [here](https://josiasaurel.github.io/python-hashnode)

### Dependenies
- Python 3.8 (but could work with older versions >3.4)
- requests
- graphql-core
- gql installation: `pip install --pre gql[all]`

This implements a hasnode class that could be used as such

```python
hashnode = Hashnode("myapitoken")

hashnode.get_feed("COMMUNITY")
# a response object containing your feed for the community section
```

## installation

```shell
pip install hashnode
```

Made by Josias Aurel (me)

Contributors welcome
