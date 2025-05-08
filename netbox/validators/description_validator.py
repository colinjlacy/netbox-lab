from extras.validators import CustomValidator

class DescriptionValidator(CustomValidator):
    def validate(self, instance, request):
        name = instance.__class__.__name__
        if instance.description == "":
            self.fail(f"Every {name} must have a Description")
        else:
            self.fail(f"Congrats on the new Description for your {name}: {instance.description}!")