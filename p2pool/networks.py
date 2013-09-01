from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    copperbars=math.Object(
        PARENT=networks.nets['copperbars'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=2*60*60//5, # shares
        REAL_CHAIN_LENGTH=2*60*60//5, # shares
        TARGET_LOOKBEHIND=150, # shares
        SPREAD=10, # blocks
        IDENTIFIER='d138e5b9e7923515'.decode('hex'),
        PREFIX='e206c3a24ee749b5'.decode('hex'),
        P2P_PORT=7870,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**22 - 1,
        PERSIST=True,
        WORKER_PORT=9777,
        BOOTSTRAP_ADDRS='94.237.84.48'.split(' '),
        ANNOUNCE_CHANNEL='#asdasdasdp2pool-alt',
        VERSION_CHECK=lambda v: v >= 60004,
    ),

    copperbars_testnet=math.Object(
        PARENT=networks.nets['copperbars_testnet'],
        SHARE_PERIOD=3, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='f037d5b8c7923510'.decode('hex'),
        PREFIX='8208c1a54ef649b0'.decode('hex'),
        P2P_PORT=17875,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**14 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS=' '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60004,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
