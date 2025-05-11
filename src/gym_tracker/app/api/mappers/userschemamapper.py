from gym_tracker.app.api.schemas.userschema import CreateUserSchema, UpdateUserSchema
from gym_tracker.domain.models.userdomain import CreateUserDomain, UpdateUserDomain


def create_user_schema_to_create_user_domain(user_schema: CreateUserSchema) -> CreateUserDomain:
    user_dict = user_schema.model_dump()
    return CreateUserDomain(**user_dict)


def update_user_schema_to_update_user_domain(user_schema: UpdateUserSchema) -> UpdateUserDomain:
    user_dict = user_schema.model_dump(exclude_unset=True)
    return UpdateUserDomain(**user_dict)
