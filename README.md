# address-book-app
An address book application where API users can create, update, delete addresses (CRUD), and retrieve addresses within a given distance

fast api url - http://127.0.0.1:8000/geo-loc/
test script - .\ev\Scripts\python.exe <name>.py

# Just call test_crud() with the action
# test_crud(CRUD_CREATE, PAYLOAD_MALACANAN)  # Create
# test_crud(CRUD_READ)                       # Read all
# test_crud(CRUD_READ, resource_id=1)        # Read one (future)
# test_crud(CRUD_UPDATE, PAYLOAD_UPDATED, resource_id=1)  # Update (future)
# test_crud(CRUD_DELETE, resource_id=1)      # Delete (future)