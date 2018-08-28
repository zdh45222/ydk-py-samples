#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Copy configuration for model Cisco-IOS-XR-mpls-lsd-cfg.

usage: nc-copy-config-xr-mpls-lsd-cfg-10-ydk.py [-h] [-v] device

positional arguments:
  device         NETCONF device (ssh://user:password@host:port)

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import NetconfService, Datastore
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_mpls_lsd_cfg \
    as xr_mpls_lsd_cfg
import logging


def config_mpls_lsd(mpls_lsd):
    """Add config data to mpls_lsd object."""
    pass


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    parser.add_argument("device",
                        help="NETCONF device (ssh://user:password@host:port)")
    args = parser.parse_args()
    device = urlparse(args.device)

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create NETCONF provider
    provider = NetconfServiceProvider(address=device.hostname,
                                      port=device.port,
                                      username=device.username,
                                      password=device.password,
                                      protocol=device.scheme)
    # create NETCONF service
    netconf = NetconfService()

    mpls_lsd = xr_mpls_lsd_cfg.MplsLsd()  # create object
    config_mpls_lsd(mpls_lsd)  # add object configuration

    # copy configuration to NETCONF device
    # netconf.lock(provider, Datastore.candidate)
    # netconf.copy_config(provider, Datastore.candidate, mpls_lsd)
    # netconf.commit(provider)
    # netconf.unlock(provider, Datastore.candidate)

    exit()
# End of script
