Feature: Search Google for a Celebrity
Scenario: Search google for Kobe Bryant
Given I go to "http://www.google.com"
And I fill in the textfield with "Kobe Bryant"
And I press "btnG"
Then I should see "kobebryant.com/"