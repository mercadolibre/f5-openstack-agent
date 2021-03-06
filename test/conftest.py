''' Test utilities for creation and deletion of pools via the sdk.

This fixture should be promoted to a more general library.  Probably
f5_os_test.
'''
# Copyright 2015-2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from f5.bigip import ManagementRoot
import pytest


def pytest_addoption(parser):
    parser.addoption("--bigip", action="store",
                     help="BIG-IP hostname or IP address")
    parser.addoption("--username", action="store", help="BIG-IP REST username",
                     default="admin")
    parser.addoption("--password", action="store", help="BIG-IP REST password",
                     default="admin")


@pytest.fixture
def opt_bigip(request):
    return request.config.getoption("--bigip")


@pytest.fixture
def opt_username(request):
    return request.config.getoption("--username")


@pytest.fixture
def opt_password(request):
    return request.config.getoption("--password")


#@pytest.fixture
#def bigip(opt_bigip, opt_username, opt_password, scope="module"):
#    '''bigip fixture'''
#    b = ManagementRoot(pytest.symbols.bigip_mgmt_ip,
#                       'admin', 'admin')
#    return b


@pytest.fixture
def NAT(bigip):
    n = bigip.ltm.nats.nat
    return n


def _delete_pools_members(bigip, pool_records):
    '''Get the members for the pool --> delete pool --> delete members'''
    for pr in pool_records:
        if bigip.ltm.pools.pool.exists(partition=pr.partition, name=pr.name):
            pool_inst = bigip.ltm.pools.pool.load(partition=pr.partition,
                                                  name=pr.name)
            members_list = pool_inst.members_s.get_collection()
            pool_inst.delete()
            for mem_inst in members_list:
                mem_inst.delete()


@pytest.fixture
def pool_factory():
    '''Given pool record objects, set up and teardown tests for that pool.'''
    def _setup_boilerplate(bigip, request, pool_records):
        _delete_pools_members(bigip, pool_records)
        pool_registry = {}
        members_registry = {}
        for pr in pool_records:
            pool_registry[pr.name] =\
                bigip.ltm.pools.pool.create(partition=pr.partition,
                                            name=pr.name)
            if pr.memberconfigs != (tuple(),):
                members_collection = pool_registry[pr.name].members_s
                for memconf in pr.memberconfigs:
                    members_registry[memconf.memname] =\
                        members_collection.members\
                        .create(partition=memconf.mempartition,
                                name=memconf.memname)

        def deleter():
            for member_instance in members_registry.values():
                member_instance.delete()
            for pool_instance in pool_registry.values():
                pool_instance.delete()
        request.addfinalizer(deleter)
        return pool_registry, members_registry
    return _setup_boilerplate
