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
MAX_TITLE_LENGTH: public(constant(uint256)) = 100
MAX_AUTHORS_PER_PPRINT: public(constant(uint256)) = 20
MAX_AUTHOR_NAME_LENGTH: public(constant(uint256)) = 100
MAX_ABSTRACT_LENGTH: public(constant(uint256)) = 2000
MAX_IPFS_HASH_LENGTH: public(constant(uint256)) = 46


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
    title: String[MAX_TITLE_LENGTH]
    authors: DynArray[String[100], MAX_AUTHORS_PER_PPRINT]
    abstract: String[MAX_ABSTRACT_LENGTH]
    ipfs_hash: String[MAX_IPFS_HASH_LENGTH]
    download_date: uint256


################################################################
#                            EVENTS                            #
################################################################
event PreprintAdded:
    id: indexed(uint256)
    owner: indexed(address)
    pub_date: uint256


################################################################
#                            ERRORS                            #
################################################################
INDEX_OUT_OF_BOUNDS: public(
    constant(String[40])
) = "pprint_sci: Index out of bounds"
# @todo Check for IPFS hash format -> lib for vyper? Rust crate CID


################################################################
#                         CONSTRUCTOR                          #
################################################################
@deploy
def __init__():
    ownable.__init__()
    self.pprint_count = 0


################################################################
#                      EXTERNAL FUNCTIONS                      #
################################################################
@external
def add_pprint(_title: String[MAX_TITLE_LENGTH], _authors: DynArray[String[100], MAX_AUTHORS_PER_PPRINT], _abstract: String[MAX_ABSTRACT_LENGTH], _ipfs_hash: String[MAX_IPFS_HASH_LENGTH]):
    """
    @dev Adds a new preprint to the contract.
    @param _title The title of the preprint.
    @param _authors The authors of the preprint.
    @param _abstract The abstract of the preprint.
    @param _ipfs_hash The IPFS hash of the preprint document.
    """
    # Check
    # @todo Check for IPFS hash format -> lib for vyper? Rust crate CID

    # Effect
    new_pprint: Preprint = Preprint(
        id=self.pprint_count,
        owner=msg.sender,
        title=_title,
        authors=_authors,
        abstract=_abstract,
        ipfs_hash=_ipfs_hash,
        download_date=block.timestamp
    )
    # Store the new preprint in the mapping
    self.id_to_pprint[self.pprint_count] = new_pprint
    self.pprint_count += 1

    # Interact
    log PreprintAdded(
        id=new_pprint.id,
        owner=new_pprint.owner,
        pub_date=new_pprint.download_date
    )
    

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
def get_preprints_count() -> uint256:
    """
    @dev Returns the number of preprints in the contract.
    @return The number of preprints in the contract.
    """
    return self.pprint_count
