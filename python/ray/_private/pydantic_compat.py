# flake8: noqa
import packaging.version

# Pydantic is a dependency of `ray["default"]` but not the minimal installation,
# so handle the case where it isn't installed.
try:
    import pydantic

    PYDANTIC_INSTALLED = True
except ImportError:
    pydantic = None
    PYDANTIC_INSTALLED = False


if not PYDANTIC_INSTALLED:
    BaseModel = None
    Field = None
    NonNegativeFloat = None
    NonNegativeInt = None
    PositiveFloat = None
    PositiveInt = None
    PrivateAttr = None
    StrictInt = None
    ValidationError = None
    root_validator = None
    validator = None
    is_subclass_of_base_model = lambda obj: False
else:
    from pydantic import (
        BaseModel,
        Field,
        NonNegativeFloat,
        NonNegativeInt,
        PositiveFloat,
        PositiveInt,
        PrivateAttr,
        StrictInt,
        ValidationError,
        root_validator,
        validator,
    )

    def is_subclass_of_base_model(obj):
        from pydantic import BaseModel

        return issubclass(obj, BaseModel)
