from extras.validators import CustomValidator

class RoleValidator(CustomValidator):
    def validate(self, instance, request):
        name = instance.__class__.__name__
        if instance.role_id is None:
            self.fail(f"Every {name} must have a Role")