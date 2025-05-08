package netbox.policies.change_freeze

default allow := true

default reasons := []

# Input shape:
# {
#   "site": {"name": "DM-Akron"},
#   "vlan": {"id": 1001}
# }

site_name := input.site.name
vlan_id := input.vlan.id

# Entire site is locked if site exists and its list is empty
deny[reason] if {
	locks := data.locks.sites[site_name]
	count(locks) == 0
	reason := sprintf("Site %v is under a full change freeze", [input.site.name])
}

# Specific VLAN is locked under this site
deny[reason] if {
	frozen_vlan := data.locks.sites[site_name][_]
	vlan_id == frozen_vlan
	reason := sprintf("VLAN %v at Site %v is under a change freeze", [vlan_id, input.site.name])
}

allow := false if {
	deny[_]
}

reasons := deny
