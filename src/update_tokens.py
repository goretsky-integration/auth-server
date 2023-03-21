import pathlib

import dodo
from config import load_config, setup_logging
from external_api_services import AuthService


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.toml'
    config = load_config(config_file_path)
    setup_logging(config.logging)

    auth_service = AuthService(base_url=config.external_api.auth_service_base_url)

    accounts = auth_service.get_accounts()
    dodo_is_api_account_names = {
        account.name for account in accounts
        if account.name.startswith('api')
    }

    for account_name in dodo_is_api_account_names:
        account_tokens = auth_service.get_account_tokens(account_name)
        new_account_tokens = dodo.get_new_auth_tokens(
            account_name=account_name,
            client_id=config.dodo_is_api_credentials.client_id,
            client_secret=config.dodo_is_api_credentials.client_secret,
            refresh_token=account_tokens.refresh_token,
        )
        auth_service.update_account_tokens(new_account_tokens)


if __name__ == '__main__':
    main()
