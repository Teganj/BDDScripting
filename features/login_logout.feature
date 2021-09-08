Feature: user logs in and logs out
  user logs in to the portal
  checks his profile name
  logs out


  Scenario Outline: login_logout
    When user navigates to <URL>
    And can see the <text>
    And user can type <username> and <password> and click login button
    And user can see text <login_message>
    And user click logout
    Then user can see <logout_message>

    Examples:
    | URL                                     | text    | username | password | login_message          | logout_message            |
    | https://accounts-qa-env.demo.rrilabs.co | Sign in | markey   | password | DAVID MARKEY THE BOSS2 | Click here to login again |

