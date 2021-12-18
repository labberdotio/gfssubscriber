
import logging

# logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)

import pystache

from gfsgql import GFSGQL

# 
# Main
# 
if __name__ == '__main__':

    gfs_host = "serv"
    gfs_port = "5000"
    gfs_username = None
    gfs_password = None

    gqlClient = GFSGQL(
        gfs_host = gfs_host,
        gfs_port = gfs_port,
        gfs_username = gfs_username,
        gfs_password = gfs_password,
    )

    dhcpServiceName = "nasdhcp1"

    dhcpServiceQuery = """
query dhcpServices($name: String!) {
  DHCPServices(name: $name) {
    id,
    name,
    defaultLeaseTime,
    maxLeaseTime,
    configuredMachines {
      id,
      name,
      arch,
      memory,
      cpus,
      cores,
      kernel,
      version,
      machine,
      processor,
      platform,
      system,
      vendor,
      description,
      release,
      codename,
      configuredInterfaces {
        id,
        name,
        hwaddr,
        addresses {
          id,
          name,
          address
        }
      },
      defaultInterface {
        id,
        name,
        hwaddr,
        addresses {
          id,
          name,
          address
        }
      }
    }
  }
}
    """

    dhcpServiceTemplate = """

ddns-update-style none;

{{#configuredMachines}}
{{#defaultInterface}}
{{#addresses}}
local-address {{address}};
{{/addresses}}
{{/defaultInterface}}
{{/configuredMachines}}

default-lease-time {{defaultLeaseTime}};
max-lease-time {{maxLeaseTime}};

# If this DHCP server is the official DHCP server for the local
# network, the authoritative directive should be uncommented.

option magic      code 208 = string;
option configfile code 209 = text;
option pathprefix code 210 = text;
option reboottime code 211 = unsigned integer 32;                                                                                                                                                                    
#option ipxe.no-pxedhcp 1;

option client-arch code 93 = unsigned integer 16;

"""

    dhcpService = gqlClient.gqlexec(
        dhcpServiceQuery,
        {
            "name": dhcpServiceName
        }
    )

    print(" GraphQL DATA: ")
    print(dhcpService)

    # renderer = pystache.Renderer()
    data = pystache.render(
        dhcpServiceTemplate,
        dhcpService["data"]["DHCPServices"][0]
    )

    print(" RENDERED OUTPUT: ")
    print(data)
