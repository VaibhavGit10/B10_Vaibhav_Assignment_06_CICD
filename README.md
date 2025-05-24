# 📌 Assignment 06 – DevOps: CI/CD for Flask Application using Jenkins & GitHub Actions

## 📖 Overview

This project demonstrates how to implement a **CI/CD pipeline** for a Python Flask web application using two automation platforms:

- **Jenkins** – for custom pipeline automation (self-hosted or cloud-based)
- **GitHub Actions** – for native GitHub-based CI/CD workflows

The pipeline covers the following stages:

- ✅ **Building the application**
- 🧪 **Running unit tests with Pytest**
- 🚀 **Deploying to Staging and Production environments**

---

## 🧩 Project Structure

```bash
.
├── app.py                     # Main Flask application
├── test_app.py                # Unit tests using Pytest
├── requirements.txt           # Python package dependencies
├── Jenkinsfile                # Jenkins pipeline configuration
├── .github/
│   └── workflows/
│       ├── cicd.yml         # GitHub Actions workflow for staging deployment and Production Development
├── .env                       # Environment variables (secrets/configs)
└── README.md                  # Project documentation (this file)

```

## 🔐 Define the `.env` File

Before running or deploying the Flask application, create a `.env` file in the root of your project directory with the following contents:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/
PORT=5000
```
<h3>📌 Notes</h3>

<ul>
  <li>These environment variables are <strong>common to both tasks</strong>.</li>
  <li>
    The default port for the application is <strong>5000</strong>. If you're using this default, you may omit the 
    <code>PORT</code> variable entirely.
  </li>
  <li>
    If you use a <strong>different port</strong>, ensure the following:
    <ul>
      <li>Your <code>Jenkinsfile</code> is updated to reflect the new port.</li>
      <li>Any GitHub Actions or other CI/CD workflows are updated accordingly to avoid deployment issues.</li>
    </ul>
  </li>
</ul>


<h2>📌 Task 1: Deployment With Jenkins</h2>

<ol>
  <li>
    <strong>Setup:</strong>
    <ul>
      <li>Install Jenkins on a virtual machine or use a cloud-based Jenkins service.</li>
      <li>Configure Jenkins with <code>Python</code>, <code>GitHub</code>, <code>SMTP</code> (for emailing), and any other required libraries or plugins.</li>
    </ul>
  </li>

  <li>
    <strong>Source Code:</strong>
    <ul>
      <li>Create your own Python Flask application that connects to MongoDB and includes unit tests using <code>pytest</code>. The application should use the <code>MONGO_URI</code> from a <code>.env</code> file.</li>
      <li>Alternatively, you can use an existing repository like the one referenced in this project.</li>
    </ul>
  </li>

  <li>
    <strong>Jenkins Pipeline:</strong>
    <ul>
      <li>Create a <code>Jenkinsfile</code> in the root of your Python application repository.</li>
      <li>In your Jenkins dashboard, create a pipeline project and point it to the repository containing the <code>Jenkinsfile</code>.</li>
      <li>The pipeline stages should include:
        <ul>
          <li><strong>Build:</strong> Install dependencies using <code>pip</code>.</li>
          <li><strong>Test:</strong> Run unit tests using <code>pytest</code>.</li>
          <li><strong>Deploy:</strong> If tests pass, deploy the application to a staging environment (e.g., Amazon EC2) using Docker, Nginx, or another deployment tool of your choice.</li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>Triggers:</strong>
    <ul>
      <li>Configure the pipeline to automatically trigger a new build when changes are pushed to the <code>main</code> branch.</li>
    </ul>
  </li>

  <li>
    <strong>Notifications:</strong>
    <ul>
      <li>Set up a notification system (e.g., via email) to alert you when the build process succeeds or fails.</li>
    </ul>
  </li>
</ol>

<p>
  <strong>Note:</strong> A sample <code>Jenkinsfile</code> is provided in this repository to demonstrate these configurations and achieve the described use cases.
</p>



#### 📸 Configure Jenkins Global Variables Screenshots

![Jenkins Dashboard](https://github.com/user-attachments/assets/a061aa6b-8114-4aab-83a3-82330209961a)
![Jenkins Dashboard](https://github.com/user-attachments/assets/b261f771-5532-4f0a-bcb4-74fcc7e1dacf)
![Jenkins Pipeline Config_02](https://github.com/user-attachments/assets/93968543-a62c-40f3-ac3a-2400d8a4234e)


#### 📸 Output Screenshots

![Jenkins Pipeline Config_03](https://github.com/user-attachments/assets/2d9c73d8-77c7-4938-8879-6bd37ed64015)
![Jenkins Pipeline Config_04](https://github.com/user-attachments/assets/5b95c676-5ecd-4892-9dc8-658e9d7befef)
![Jenkins Pipeline Config_05](https://github.com/user-attachments/assets/c250e86c-17f9-4705-be2e-fc4328e32fad)
![Jenkins Pipeline Config_06](https://github.com/user-attachments/assets/11a7368f-1470-4e13-99a7-4d7f5fb17f3d)
![Jenkins_Git_Hook_Trigger_Pipeline Config_07](https://github.com/user-attachments/assets/61b029cf-9bd8-4c83-9329-986f40d4709f)
![Git_webhook_Congif](https://github.com/user-attachments/assets/86d16d4d-7bc2-48fa-957f-4717b8dd5247)
![Git_webhook_Config_02](https://github.com/user-attachments/assets/140df8aa-3652-4726-9e75-31e2551f859b)
![Git_webhook_Config_Testing_01](https://github.com/user-attachments/assets/8c4fa9d3-4756-490e-b6ca-7b8afb29c083)
![Git_webhook_Config_Testing_02](https://github.com/user-attachments/assets/2b64f675-9d1d-4ac9-a390-6980829593c1)
![Jenkins_Pipeline_Success_01](https://github.com/user-attachments/assets/a7a7e0cb-b0f9-4799-9bda-d6997faa4ed5)
![Jenkins_Pipeline_Success_02](https://github.com/user-attachments/assets/08fa6ddb-02aa-4c09-857e-be7745fbc7ea)
![Jenkins_Pipeline_Success_03](https://github.com/user-attachments/assets/dcfe2a50-30d9-4feb-9dbc-8b03ea0c4105)
![Jenkins_Pipeline_Success_04](https://github.com/user-attachments/assets/971314c8-efcd-4b09-81b5-19ec297b9110)
![Jenkins_Pipeline_Success_05](https://github.com/user-attachments/assets/aa02631a-0fcf-4b21-ae12-6c00bca3de6c)
![Flask_App_run](https://github.com/user-attachments/assets/14809c0b-39ce-4a33-aec5-6dd08ec02a65)
![Jenkins_Mail_Success](https://github.com/user-attachments/assets/29dcbd64-6556-4b8f-9ae7-7834abb45776)


<h1>📌 Task 2: Deployment With GitHub Actions</h1>

<h2>1. Setup</h2>
<ul>
  <li>Create a Python Flask application that connects to MongoDB.</li>
  <li>Use <code>MONGO_URI</code> stored in a <code>.env</code> file for the database connection.</li>
  <li>Include <code>pytest</code> test cases to verify your application functionality.</li>
  <li>Ensure your Git repository has both a <code>main</code> branch and a <code>staging</code> branch.</li>
  <li>You can either create your own app or use an existing repo similar to the referenced example.</li>
</ul>

<hr />

<h2>2. GitHub Actions Workflow</h2>
<ul>
  <li>Create a <code>.github/workflows</code> directory inside your repository, specifically in the <code>staging</code> branch.</li>
  <li>Inside this directory, create a YAML file (for example, <code>ci-cd.yml</code>) to define the GitHub Actions workflow.</li>
</ul>

<hr />

<h2>3. Workflow Jobs and Steps</h2>

<h3>Install Dependencies</h3>
<ul>
  <li>Use Python and <code>pip</code> to install all required dependencies for your Flask app.</li>
  <li>Example: <code>pip install -r requirements.txt</code></li>
</ul>

<h3>Run Tests</h3>
<ul>
  <li>Run your test suite with <code>pytest</code> to verify that your code works correctly.</li>
  <li>The workflow should fail if any tests fail.</li>
</ul>

<h3>Build</h3>
<ul>
  <li>If tests pass, prepare the application for deployment (e.g., packaging or building a Docker image).</li>
</ul>

<h3>Deploy to Staging</h3>
<ul>
  <li>Automatically deploy the app to a <strong>staging environment</strong> when changes are pushed to the <code>staging</code> branch.</li>
  <li>This allows preview and verification of changes before going live.</li>
</ul>

<h3>Deploy to Production</h3>
<ul>
  <li>Deploy the app to the <strong>production environment</strong> when a release is tagged in the repository.</li>
  <li>This ensures controlled, versioned releases.</li>
</ul>

<hr />

<h2>4. Managing Environment Secrets</h2>
<ul>
  <li>Store sensitive information (such as deployment keys, API tokens, or MongoDB connection URIs) securely in <strong>GitHub Secrets</strong>.</li>
  <li>Use these secrets in your workflow YAML to access credentials without exposing them in the codebase.</li>
</ul>

<hr />


#### 📸 Configure Github Secrets Screenshot

![image](https://github.com/user-attachments/assets/43667091-c3c6-49fc-ae5e-fce79ee9469d)


#### 📸 Output Screenshots

![Git_Actions_01](https://github.com/user-attachments/assets/5aca4c88-1cf0-42b0-b0af-bc0ec4a5dff2)
![Git_Actions_02](https://github.com/user-attachments/assets/71a547eb-9fb9-4f62-a0dc-10962c99f69e)
![Git_Actions_03](https://github.com/user-attachments/assets/5c2da4cc-dd5c-48e6-9c5e-762f8c92a719)
![Git_Actions_04](https://github.com/user-attachments/assets/63bcc628-0e1a-44a8-acee-b44bcbb64c5a)
![Git_Actions_05](https://github.com/user-attachments/assets/d4aee69c-6493-43bb-ba2d-1ef5107926ee)
![Git_Actions_06](https://github.com/user-attachments/assets/34579897-0fa2-49b9-9218-e1bcbfab99fd)
![Git_Actions_07](https://github.com/user-attachments/assets/556f6dc4-837e-4b1c-b561-92703714df5f)
![Git_Actions_08](https://github.com/user-attachments/assets/549c0598-4dfc-4345-89d7-6f0f3113a2c9)
![Git_Actions_09](https://github.com/user-attachments/assets/b115ec12-4ddf-4a1c-abb6-870374762e9f)
![Git_Actions_10](https://github.com/user-attachments/assets/d8b47bf3-8fad-45b9-834e-79406556c958)
![Git_Actions_11](https://github.com/user-attachments/assets/276f883c-d69a-443f-be45-fcfad89105c1)
![Git_Actions_12](https://github.com/user-attachments/assets/e26b9dce-7fb4-4763-96ad-64132f0b46c2)
![Git_Actions_13](https://github.com/user-attachments/assets/800894eb-a8d7-4bd4-ae26-887dcfe3a18f)
![Git_Actions_14](https://github.com/user-attachments/assets/441a9c54-4f8e-4853-903c-3007ef740dc5)

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT), allowing you to freely use, modify, and distribute the code with proper attribution.

---

## 🤝 Contributing

Contributions are highly welcome! Feel free to fork the repository, suggest improvements, and submit pull requests. ⭐

If you find this project helpful, please consider giving it a star — your support motivates me to keep improving and maintaining this work. Thank you! 😊

---

## 📧 Contact

Have questions, feedback, or ideas? Please open an issue on GitHub — I’m happy to connect and collaborate!

---

🎯 **Thank you for taking the time to review this project! Your interest and support mean a lot. Let’s build something amazing together! 🚀**

