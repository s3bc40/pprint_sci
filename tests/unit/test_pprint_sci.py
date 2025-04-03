from moccasin.boa_tools import VyperContract
from eth.constants import ZERO_ADDRESS
from script.deploy import deploy_pprint


def test_deploy_contract():
    # Arrange
    contract: VyperContract = deploy_pprint()

    # Act/Assert
    assert contract.address != ZERO_ADDRESS
