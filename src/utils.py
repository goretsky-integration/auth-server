import json

import config


def read_accounts_file() -> list[dict]:
    """Read accounts.json file in the root of repo.

    Returns:
        List of account objects.
    """
    with open(config.ACCOUNTS_FILE_PATH, encoding='utf-8') as accounts_file:
        return json.load(accounts_file)
