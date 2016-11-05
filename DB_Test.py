import Utility

#testing all db related functions


print("TEST_START - Processing: Testing DB input...")
x = 8 #test input
Utility.DB_Input(x);
print("TEST_END - Success: Input test passed")

print("TEST_START - Processing: Testing DB print...")
Utility.DB_PrintAll();
print("TEST_END - Success: Print test passed")

#will add more