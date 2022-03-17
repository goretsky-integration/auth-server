import time

import authenticator
import config
import dodo_account


def main():
    all_accounts = dodo_account.get_dodo_accounts()
    while True:
        accounts = dodo_account.filter_accounts_with_expired_cookies(all_accounts)
        for account in accounts:
            authenticator.update_account_cookies(account)
            time.sleep(1)
        time.sleep(config.COOKIES_UPDATE_DELAY)


if __name__ == '__main__':
    main()
