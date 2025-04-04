import pytest

from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network
from moccasin.moccasin_account import MoccasinAccount
from script.deploy import deploy_pprint


################################################################
#                             UNIT                             #
################################################################
@pytest.fixture(scope="function")
def account_sender() -> MoccasinAccount:
    """Get deployer entity from default network."""
    return get_active_network().get_default_account()


@pytest.fixture(scope="function")
def pprint_contract() -> VyperContract:
    """Fixture to deploy the pprint_sci contract."""
    return deploy_pprint()
