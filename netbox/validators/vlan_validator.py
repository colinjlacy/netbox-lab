import requests
from extras.validators import CustomValidator

class VlanValidator(CustomValidator):
    def validate(self, vlan, request):
        from ipam.models import VLAN
        if vlan.site_id is not None:
            site_id = vlan.site_id
            name = vlan.name
            exists = VLAN.objects.filter(site_id=site_id, name=name).exists()
            if exists:
                self.fail("A VLAN with the specified site_id and name exists.")

        # self._check_has_role(vlan)

    # def _check_name_unique_for_site(self, vlan, request):
    #     from ipam.models import VLAN
    #     if vlan.site_id is not None:
    #         site_id = vlan.site_id
    #         name = vlan.name
    #         exists = VLAN.objects.filter(site_id=site_id, name=name).exists()
    #         if exists:
    #             self.fail("A VLAN with the specified site_id and name exists.")
    #         else:
    #             self.fail("No VLAN with the specified site_id and name exists.")

    def _check_has_role(self, vlan):
        if vlan.role_id is None:
            self.fail("Every VLAN must have a Role")
        else:
            self.fail("Congrats on the new Role!")


class VlanDeleteValidator(CustomValidator):
    def validate(self, vlan, request):
        v = vlan
        self.fail("No VLAN with the specified site_id and name exists.")


class VlanChangeFreezeValidator(CustomValidator):
    def validate(self, vlan, request):
        input_data = {
            "vlan": {"id": vlan.id},
            "site": {"name": vlan.site.name if vlan.site else None}
        }

        response = requests.post(
            "http://localhost:8181/v1/data/netbox/policies/change_freeze/allow",
            json={"input": input_data},
            timeout=2,
        )

        if not response.ok or not response.json().get("result", True):
            # Optionally fetch reasons
            reasons_response = requests.post(
                "http://localhost:8181/v1/data/netbox/policies/change_freeze/reasons",
                json={"input": input_data},
                timeout=2,
            )
            reason = reasons_response.json().get("result", "Policy denied the operation")
            self.fail(list(reason.keys())[0])
