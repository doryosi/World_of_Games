The Project is a console based game application.

The user choose 1 of 3 games available to play.
At the end the user's score are saved into a score file which is presented in a web page using Flask framework.

There is a jenkins file written to automate the CI/CD pipeline using the following stages:
 - Checkout
 - Build
 - Run
 - Test
 - Push
If the Jenkins Job succeed, then the docker image is saved to docker hub.
