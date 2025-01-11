Feature: DemoQA API Testing

  Scenario: Create user, generate token, and rent books
    Given I create a new user
    When I generate a token for the user
    Then I confirm the user is authorized
    And I list available books
    And I rent two random books
    Then I verify the user details with rented books
