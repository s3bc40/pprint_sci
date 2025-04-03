# pragma version 0.4.1
"""
@title Pretty Print Sci - A simple pre printer for scientific documentation
@license MIT
@author s3bc40
@dev
    This project aims to create a basic, decentralized version of a pre-print server.
    Instead of storing the pre-print documents themselves on the blockchain (which would be very expensive),
    we'll focus on storing the metadata of the pre-prints on a Vyper smart contract.
    The actual documents will be stored on IPFS (InterPlanetary File System), a decentralized storage network.
"""
################################################################
#                           IMPORTS                            #
################################################################
from snekmate.auth import ownable


################################################################
#                           MODULES                            #
################################################################
initializes: ownable
exports: ownable.owner


################################################################
#                          CONSTANTS                           #
################################################################
MAX_PPRINTS_PER_OWNER: constant(uint256) = 300
MAX_AUTHORS_PER_PPRINT: constant(uint256) = 10


################################################################
#                       STATE VARIABLES                        #
################################################################
pprint_count: uint256
id_to_pprint: HashMap[uint256, Preprint]


################################################################
#                           STRUCTS                            #
################################################################
# @dev A struct to represent a preprint document.
# It contains the title, authors, abstract, IPFS hash, and publication date.
# The IPFS hash is a unique identifier for the document stored on IPFS.
# The publication date is stored as a uint256 timestamp.
struct Preprint:
    id: uint256
    owner: address
    title: String[100]
    authors: DynArray[String[100], MAX_AUTHORS_PER_PPRINT]
    abstract: String[1000]
    ipfs_hash: String[100]
    publication_date: uint256


################################################################
#                            ERRORS                            #
################################################################
INDEX_OUT_OF_BOUNDS: public(
    constant(String[40])
) = "pprint_sci: Index out of bounds"


################################################################
#                         CONSTRUCTOR                          #
################################################################
@deploy
def __init__():
    ownable.__init__()
    self.pprint_count = 0


################################################################
#                   EXTERNAL VIEW FUNCTIONS                    #
################################################################
@view
@external
def get_pprint_by_id(_id: uint256) -> Preprint:
    """
    @dev Returns the preprint with the specified ID.
    @param _id The ID of the preprint to retrieve.
    @return The preprint with the specified ID.
    """
    assert _id < self.pprint_count, INDEX_OUT_OF_BOUNDS
    return self.id_to_pprint[_id]


@view
@external
def get_owned_preprints_count() -> uint256:
    """
    @dev Returns the number of preprints in the contract.
    @return The number of preprints in the contract.
    """
    return self.pprint_count
