from datetime import timedelta

from rest_framework.serializers import ChoiceField


class DurationChoicesField(ChoiceField):
    default_error_messages = {
        'invalid_value': '"{input}" is not a valid value.'
    }

    def to_internal_value(self, data):
        try:
            duration = timedelta(seconds=float(data))
        except ValueError:
            self.fail('invalid_value', input=data)

        return super().to_internal_value(duration)
