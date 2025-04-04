import boa

from tests.constants import (
    AUTHORS,
    ABSTRACT,
    IPFS_HASH,
    TITLE,
)
from moccasin.boa_tools import VyperContract
from eth.constants import ZERO_ADDRESS
from script.deploy import deploy_pprint
from typing import NamedTuple


class Preprint(NamedTuple):
    """Preprint structure."""

    id: int
    owner: str
    title: str
    authors: list[str]
    abstract: str
    ipfs_hash: str
    download_date: int


################################################################
#                             INIT                             #
################################################################
def test_deploy_contract(account_sender):
    # Arrange
    contract: VyperContract = deploy_pprint()

    # Act/Assert
    assert contract.address != ZERO_ADDRESS
    assert contract.owner() == account_sender.address


def test_no_preprint_struct_at_init(pprint_contract, account_sender):
    # Arrange/Act/Assert
    assert pprint_contract.owner() == account_sender.address
    assert pprint_contract.get_preprints_count() == 0
    with boa.reverts(pprint_contract.INDEX_OUT_OF_BOUNDS()):
        pprint_contract.get_pprint_by_id(0) is None


################################################################
#                          ADD PPRINT                          #
################################################################
def test_add_pprint_struct(pprint_contract, account_sender):
    # Arrange
    expected_id = 0
    expected_title = TITLE
    expected_authors = AUTHORS
    expected_abstract = ABSTRACT
    expected_ipfs_hash = IPFS_HASH
    expected_download_date = boa.env.timestamp

    # Act
    pprint_contract.add_pprint(
        expected_title, expected_authors, expected_abstract, expected_ipfs_hash
    )
    logs = pprint_contract.get_logs()

    # Assert
    # Log check
    assert len(logs) == 1
    assert logs[0].id == expected_id
    assert logs[0].owner == account_sender.address
    assert logs[0].pub_date == expected_download_date

    # Preprint check
    assert pprint_contract.get_preprints_count() == 1
    pprint: Preprint = pprint_contract.get_pprint_by_id(expected_id)
    assert pprint is not None
    assert pprint.id == expected_id
    assert pprint.owner == account_sender.address
    assert pprint.title == expected_title
    assert pprint.authors == expected_authors
    assert pprint.abstract == expected_abstract
    assert pprint.ipfs_hash == expected_ipfs_hash
    assert pprint.download_date == expected_download_date


def test_add_pprint_title_too_long(pprint_contract):
    # Arrange
    expected_title = "a" * (pprint_contract.MAX_TITLE_LENGTH() + 1)
    expected_authors = AUTHORS
    expected_abstract = ABSTRACT
    expected_ipfs_hash = IPFS_HASH

    # Act/Assert
    with boa.reverts():
        pprint_contract.add_pprint(
            expected_title, expected_authors, expected_abstract, expected_ipfs_hash
        )


def test_add_pprint_authors_name_too_long(pprint_contract):
    # Arrange
    expected_title = TITLE
    expected_authors = ["a" * (pprint_contract.MAX_AUTHOR_NAME_LENGTH() + 1)]
    expected_abstract = ABSTRACT
    expected_ipfs_hash = IPFS_HASH

    # Act/Assert
    with boa.reverts():
        pprint_contract.add_pprint(
            expected_title, expected_authors, expected_abstract, expected_ipfs_hash
        )


def test_add_pprint_authors_too_many(pprint_contract):
    # Arrange
    expected_title = TITLE
    expected_authors = [
        "a" * pprint_contract.MAX_AUTHOR_NAME_LENGTH()
        for _ in range(pprint_contract.MAX_AUTHORS_PER_PPRINT() + 1)
    ]
    expected_abstract = ABSTRACT
    expected_ipfs_hash = IPFS_HASH

    # Act/Assert
    with boa.reverts():
        pprint_contract.add_pprint(
            expected_title, expected_authors, expected_abstract, expected_ipfs_hash
        )


def test_add_pprint_abstract_too_long(pprint_contract):
    # Arrange
    expected_title = TITLE
    expected_authors = AUTHORS
    expected_abstract = "a" * (pprint_contract.MAX_ABSTRACT_LENGTH() + 1)
    expected_ipfs_hash = IPFS_HASH

    # Act/Assert
    with boa.reverts():
        pprint_contract.add_pprint(
            expected_title, expected_authors, expected_abstract, expected_ipfs_hash
        )


def test_add_pprint_ipfs_hash_too_long(pprint_contract):
    # Arrange
    expected_title = TITLE
    expected_authors = AUTHORS
    expected_abstract = ABSTRACT
    expected_ipfs_hash = "a" * (pprint_contract.MAX_IPFS_HASH_LENGTH() + 1)
    # Act/Assert
    with boa.reverts():
        pprint_contract.add_pprint(
            expected_title, expected_authors, expected_abstract, expected_ipfs_hash
        )
