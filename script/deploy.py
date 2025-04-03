from moccasin.boa_tools import VyperContract
from contracts import pprint_sci


def deploy_pprint() -> VyperContract:
    """Deploys the pprint_sci contract."""
    return pprint_sci.deploy()


def moccasin_main() -> VyperContract:
    """Main equivalent for moccasin."""
    return deploy_pprint()
