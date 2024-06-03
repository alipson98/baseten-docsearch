# baseten-docsearch

This is a toy doc search truss on Baseten

Usage:
`truss predict -d '{"query": "Sentence similar to desired results", "offset": 2, "limit": 4}'`

Currently all "documents" are just a python list of strings, not stored in a vector DB. The next phase will be to store in the db so we can keep much larger datasets
