


















def fake_patch_req(user_id, **kwargs):

    print(f"Updating resource with ID {user_id}")

    print(f"UPDATING RECORD: \n\n")  # noqa: F541
    for key, value in kwargs.items():
        print(f"Updating {key} to {value}")

    return {
        "status": "success",
        "message": f"Resource {user_id} updated successfully",
        "updated_fields": kwargs
    }

response = fake_patch_req(
    user_id=123,
    # name="New Resource Name",
    # spot_name="Disney world",
    description="Updated description",
    is_active=True
)

# print("\nResponse:", response)
