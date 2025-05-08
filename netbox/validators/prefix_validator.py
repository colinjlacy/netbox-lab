from extras.validators import CustomValidator

class PrefixValidator(CustomValidator):
    def validate(self, prefix, request):
        if str(prefix).startswith("127"):
            self.fail("No local prefixes allowes!", field="prefix")

class PrefixDeleteValidator(CustomValidator):
    def validate(self, prefix, request):
        # Example: prevent deletion if prefix has child prefixes
        if prefix.get_children().exists():
            self.fail("This prefix has child prefixes and cannot be deleted.")

        # Example: prevent deletion if prefix has any assigned IPs
        if prefix.get_assigned_ips().exists():
            self.fail("This prefix has assigned IP addresses and cannot be deleted.")