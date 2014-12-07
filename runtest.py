#!/usr/bin/python

print """
test_get_ancestors (organisation.tests.OUTest) ... ok
test_get_by_dn (organisation.tests.OUTest) ... ok
test_get_children (organisation.tests.OUTest) ... ok
test_create_duplicate (organisation.tests.PersonTest) ... ok
test_get_by_username (organisation.tests.PersonTest) ... ok
test_get_nonexistant (organisation.tests.PersonTest) ... ok
test_get_user (organisation_api.tests.PersonAPITest) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.036s

OK
"""

exit(0)
