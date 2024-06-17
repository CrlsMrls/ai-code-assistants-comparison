# Fix security issues in a Java-based backend service

In this project, you will fix issues in a Java-based backend service that provides a file upload functionality. The backend service is a clone from the [Spring Boot Uploading Files guide](https://spring.io/guides/gs/uploading-files). The introductory guide walks on the steps to create a Spring Boot application that provides a REST API to upload files. 

Here, the goal is to ask the AI Code assistant what security issues it may find, how to fix them and add unit tests to verify that those security issues are fixed.

## Setup and run the project

Verify that you have Java JDK 17 installed with `javac -version` command. If you don't have Java installed, you can download it from the [OpenJDK website](https://adoptopenjdk.net/).

### Build and run the project with Gradle
To build the project, in the directory where the project is located, run the following command:

```bash
./gradlew build

> Task :compileTestJava
...

BUILD SUCCESSFUL in 17s
8 actionable tasks: 8 executed
```

To run the project, run the following command:

```bash
./gradlew bootRun --continuous

...
Tomcat started on port 8080 (http) with context path ''
...
```

Open the following URL in your browser: http://localhost:8080

Make sure the application works, by uploading a small file and verifying that it is stored in the `filestorage` directory. If an HTTP 413 error is returned, it means that the file is too large. You could try with the file `small-file.svg` which is small enough.

### Test the project

To run the tests, run the following command:

```bash
./gradlew test

BUILD SUCCESSFUL in 25s
5 actionable tasks: 3 executed, 2 up-to-date
```

## AI Code assistant

The original project is focused on building a basic file upload service using Spring Boot. There are practically no security checks. The AI Code assistant should help you to identify and fix them.

Will the AI Code assistant be able to find the security issues in the code? Which one will be better?

To be fair, you should use the same prompt for all AI Code assistants. This way, you can compare the results and see which one is better at finding the security issues. The following prompts are a starting point, but feel free to adjust them as needed.

### Initial prompt

Let's focus first on identifying the security issues in the code. Open the file `src/main/java/com/filestorage/FileStorageController.java` and using the AI Code assistant chat paste the following prompt:

```text
You are an Java expert developer, with special focus on security. You have been asked to review the file upload functionality in the FileStorageController class. There are some issues in the code. Can you help me fix the issues? 

For each issue you may find, could provide a short description on how to fix it? There is no need to provide the code. A follow-up question will be asked to provide the code.
```

### Follow-up prompt

The AI Code Assistant should detect the **transversal directory attack**. This issue could allow an attacker to overwrite critical system files. To fix this issue, you should sanitize the filename before saving it to the server.


```text
The code does not protect against path traversal attacks. How can I fix this issue?

Could you provide the code to fix the issue? and the two unit tests, one to verify that an invalid filename is sanitized and provides an error, the second unit test verifies that a valid filename is not sanitized and is saved correctly.
```

Make sure to test the code and verify that the issue is fixed by running the tests (`./gradlew test`).

### Common follow-ups

- **File size limit**: There is already a file size limit in the code. The AI Code assistant should detect this. The tricky part is the code is Spring Boot specific, and not part of the code. Will the AI Code Assistant detect the `spring.servlet.multipart.max-file-size` property or suggest a new solution?

- **File type validation**: The code does not validate the file type. A simple task would be to ask the AI Code assistant to provide a solution to validate the file type.

- **Overwriting files**: The code does not check if the file already exists. The AI Code assistant should detect this issue and suggest a solution too.