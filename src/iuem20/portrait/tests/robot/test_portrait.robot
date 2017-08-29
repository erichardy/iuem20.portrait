# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s iuem20.portrait -t test_portrait.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src iuem20.portrait.testing.IUEM20_PORTRAIT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_portrait.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a portrait
  Given a logged-in site administrator
    and an add portrait form
   When I type 'My portrait' into the title field
    and I submit the form
   Then a portrait with the title 'My portrait' has been created

Scenario: As a site administrator I can view a portrait
  Given a logged-in site administrator
    and a portrait 'My portrait'
   When I go to the portrait view
   Then I can see the portrait title 'My portrait'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add portrait form
  Go To  ${PLONE_URL}/++add++portrait

a portrait 'My portrait'
  Create content  type=portrait  id=my-portrait  title=My portrait


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the portrait view
  Go To  ${PLONE_URL}/my-portrait
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a portrait with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the portrait title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
