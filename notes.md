1. NULL Platform_Id Error

While creating a Many to Many relationship, I had to revert the data to list like which I believed cause an error with the data for the Parent table.

2. CLI ModuleNotFoundError: No module named

Creating multi models file for each SCHEMA Class causes ModuleNotFoundError: No module named.
Even and declare the path for each individual Models errors still occured.
Reverting back to a single model file resolved error

3. Module issue with cli.py not importing models if in different directory
