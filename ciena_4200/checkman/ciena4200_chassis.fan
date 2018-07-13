title: Ciena 4200: Chassis fans
catalog: unsorted
agents: snmp
license: GPL
distribution: Techfu NMS
description:
 This check collects chassis fan information from Ciena 4200 chassis
 via SNMP mib IPI-GSLAMAG-MIB.

item:
 Each fan is shown as numbered on the device. E.g.
 {Fan 1}

inventory:
 The inventory creates a service for each fan slot in the chassis.

