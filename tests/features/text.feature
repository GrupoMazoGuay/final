

Feature: User introduces text in text box

  Scenario: User introduces URL
    Given I have the string "https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt"
    When Push execute
    Then I see results

  Scenario: User introduces invalid URL
    Given I have the string "e"
    When Push execute
    Then I see not results

  Scenario: User introduces emply URL
    Given I have the string ""
    When Push execute
    Then I see not results

  Scenario: User introduces URL
    Given I have the string "https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt"
    And Push execute
    And I have the string "e"
    When Push execute
    Then I see results