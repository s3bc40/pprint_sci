from moccasin.config import get_active_network, Network
from moccasin.boa_tools import VyperContract
from contracts import pprint_sci


def deploy_pprint() -> VyperContract:
    """Deploys the pprint_sci contract."""
    active_network: Network = get_active_network()
    if not active_network.is_local_or_forked_network() and active_network.has_explorer():
        # Contract verification on block explorer
        result = active_network.moccasin_verify()
        result.wait_for_verification()
    return pprint_sci.deploy()


def moccasin_main() -> VyperContract:
    """Main equivalent for moccasin."""
    return deploy_pprint()
