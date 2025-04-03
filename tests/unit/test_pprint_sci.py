import boa

from moccasin.boa_tools import VyperContract
from eth.constants import ZERO_ADDRESS
from script.deploy import deploy_pprint


def test_deploy_contract(account_sender):
    # Arrange
    contract: VyperContract = deploy_pprint()

    # Act/Assert
    assert contract.address != ZERO_ADDRESS
    assert contract.owner() == account_sender.address


def test_no_preprint_struct_at_init(pprint_contract, account_sender):
    # Arrange/Act/Assert
    assert pprint_contract.owner() == account_sender.address
    assert pprint_contract.get_owned_preprints_count() == 0
    with boa.reverts(pprint_contract.INDEX_OUT_OF_BOUNDS()):
        pprint_contract.get_pprint_by_id(0) is None
