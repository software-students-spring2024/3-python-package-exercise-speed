# Contributing to PyDancer

Welcome to **PyDancer**! We appreciate your interest in helping make our Python library better. Here are some guidelines to get you started:

## Reporting Issues

If you encounter any bugs, issues, or have suggestions for improvements, please report them on the GitHub Issues page. Be sure to provide detailed information, including steps to reproduce the issue and any error messages received.

## How to Contribute

If you'd like to contribute code, add documentation, or add tests, you can do so by submitting a pull request. Here's how you can get started:

1. **Fork the Repository**: Click the "Fork" button in the top-right corner of the GitHub page to create your own copy of the repository.

2. **Clone the Repository**: Clone your fork of the repository to your local machine using the following command:
   ```
   git clone https://github.com/<your-username>/3-python-package-exercise-speed.git
   ```

3. **Navigate to the Project Directory**: Change into the project directory:
    ```
    cd 3-python-package-exercise-speed
    ```

4. **Set Up Upstream**
    Set the remote name upstream to point to the main repository

    ```
    git remote add upstream https://github.com/software-students-spring2024/3-python-package-exercise-speed.git
    ```

    You can now use upstream to retrieve the current source code. You should fetch the upstream changes from GitHub from time to time:

    ```
    git fetch upstream
    ```

5. **Set Up a Virtual Environment**

    We recommend using pipenv to manage dependencies and create a virtual environment for the project. If you don't have pipenv installed, you can install it using pip:

    ```
    pip install pipenv
    ```

    Then, create a virtual environment for the project:
    ```
    pipenv shell
    ```
    This command will create a virtual environment and activate it.

    With the virtual environment activated, install the project dependencies:

    ```
    pipenv install
    ```

    This command will install all the required packages listed in the Pipfile.lock file.

    
6. **Create a Branch**: Create a new branch for your changes using a descriptive name. For example:
   ```
   git checkout -b <feature-name>
   ```

7. **Make Changes**: Make your desired changes to the codebase. Whether it's fixing a bug, adding a new feature, or improving documentation, your contributions are welcome!

8. **Test Your Changes**: Ensure that your changes don't introduce any errors and that existing functionality still works as expected.

9. **Commit Your Changes**: Once you're happy with your changes, commit them to your branch with descriptive commit messages:
   ```
   git add .
   git commit -m "Add new feature: Description of your changes"
   ```

10. **Push Changes**: Push your changes to your fork on GitHub:
    ```
    git push origin <feature-name>
    ```

11. **Create a Pull Request**: Go to the GitHub page of your forked repository and click the "New pull request" button. Provide a clear description of your changes and submit the pull request.

12. **Review and Merge**: After submitting a pull request, your changes will be reviewed by the project maintainers. Once approved, they will be merged into the main codebase.

Thank you for your interest in contributing to PyDancer! We appreciate your help in making this project better for everyone.