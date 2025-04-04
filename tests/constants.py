################################################################
#                          TEST UNIT                           #
################################################################
# Working
TITLE = "Statistical analysis of spatial patterns in tumor microenvironment images"
AUTHORS = [
    "Mohamed M. Benimam",
    "Vannary Meas-Yedid",
    "Suvadip Mukherjee",
    "Astri Frafjord",
    "Alexandre Corthay",
    "Thibault Lagache",
    "Jean-Christophe Olivo-Marin",
]
ABSTRACT = """Advances in tissue labeling, imaging, and automated cell identification now
enable the visualization of immune cell types in human tumors. However, a
framework for analyzing spatial patterns within the tumor microenvironment
(TME) is still lacking. To address this, we develop Spatiopath, a null-hypothesis
framework that distinguishes statistically significant immune cell associations
from random distributions. Using embedding functions to map cell contours
and tumor regions, Spatiopath extends Ripley’s K function to analyze both cellcell and cell-tumor interactions. We validate the method with synthetic
simulations and apply it to multi-color images of lung tumor sections,
revealing significant spatial patterns such as mast cells accumulating near T
cells and the tumor epithelium. These patterns highlight differences in spatial
organization, with mast cells clustering near the epithelium and T cells positioned farther away. Spatiopath enables a better understanding of immune
responses and may help identify biomarkers for patient outcomes."""
IPFS_HASH = "QmaPjeqYAzkfm8hJzkwdCCSQPmpJDkFRrYuDmX31nV7Y7P"  # V0 hash
