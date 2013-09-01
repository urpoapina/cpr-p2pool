import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack
from operator import *

def debug_block_info(dat1):
	print 'block header',  data.block_header_type.unpack(dat1)['timestamp']
	return 0

nets = dict(
    copperbars=math.Object(
        P2P_PREFIX='d9e6e7e5'.decode('hex'),
        P2P_PORT=7874,
        ADDRESS_VERSION=28,
        RPC_PORT=7873,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'copperbarsaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.0064*1000000,
        BLOCKHASH_FUNC=lambda header: pack.IntType(256).unpack(__import__('cpr_scrypt').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        POW_FUNC=lambda header: pack.IntType(256).unpack(__import__('cpr_scrypt').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        BLOCK_PERIOD=10, # s
        SYMBOL='CPR',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'copperbars') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/copperbars/') if platform.system() == 'Darwin' else os.path.expanduser('~/.copperbars'), 'copperbars.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://x/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://x/address/',
        SANE_TARGET_RANGE=(2**256//2**20//1000 - 1, 2**256//2**22 - 1),
    ),

    copperbars_testnet=math.Object(
        P2P_PREFIX='cdf2c0ef'.decode('hex'),
        P2P_PORT=10002,
        ADDRESS_VERSION=111,
        RPC_PORT=10001,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'copperbarsaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 0.0064*100000,
        BLOCKHASH_FUNC=lambda header: pack.IntType(256).unpack(__import__('yac_scrypt_test').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        POW_FUNC=lambda header: pack.IntType(256).unpack(__import__('yac_scrypt_test').getPoWHash(header, data.block_header_type.unpack(header)['timestamp'])),
        BLOCK_PERIOD=6, # s
        SYMBOL='tCPR',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'YaCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/YaCoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.copperbars'), 'test1.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://nonexistent-yacoin-testnet-explorer/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://nonexistent-yacoin-testnet-explorer/address/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
