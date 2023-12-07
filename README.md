<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>AssistantsGPTMngt</h1>
<h3>◦ Gain control on your assistants</h3>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat-square&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />
</p>
<img src="https://img.shields.io/github/license/hansipie/AssistantsGPTMngt?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/hansipie/AssistantsGPTMngt?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/hansipie/AssistantsGPTMngt?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/hansipie/AssistantsGPTMngt?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents
- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running AssistantsGPTMngt](#-running-AssistantsGPTMngt)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

AssistantsGPTMngt is a code repository containing an Assistants Management application. It uses Streamlit library to create a web-based interface, allowing users to input their OpenAI API key and manage their assistants. The app displays existing assistants in a tabular format, allowing users to select assistants for deletion. It provides a user-friendly way to manage and delete assistants using the OpenAI library.

---

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a simple architecture with a single file, app.py, which serves as the main entry point for the application. It uses the Streamlit library to create a web-based interface. The codebase implements a basic client-server architecture, where the user interacts with the application through the web interface served by Streamlit, and the server-side logic is handled by the code in app.py. |
| 📄 | **Documentation**  | The codebase is lacking comprehensive documentation. Although there are code summaries for the app.py and requirements.txt files, there is no separate documentation file or detailed comments within the codebase. Adding more detailed explanations, function and class-level comments, and a separate README file would greatly improve the comprehensiveness of the documentation. |
| 🔗 | **Dependencies**   | The codebase has a few external dependencies, including the Python programming language itself, as well as the Streamlit, streamlit-file-browser, and openai libraries. The requirements.txt file specifies these dependencies and can be used to easily install all the required libraries for running the application. |
| 🧩 | **Modularity**     | The codebase is organized into a single file, app.py, which contains all the logic for the application. However, the code can be further modularized by separating different functionalities into separate modules or classes. This would improve code maintainability and reusability. |
| 🧪 | **Testing**        | The codebase does not have any explicit testing strategies or tools implemented. Adding unit tests, integration tests, and possibly automated testing tools like pytest or unittest would greatly improve the overall quality and robustness of the codebase. |
| ⚡️  | **Performance**    | The performance of the system depends on the efficiency of the Streamlit framework and the response times of the OpenAI API. The codebase itself does not have any specific performance optimizations. Considering the code's simplicity and the fact that it primarily relies on external services, the performance should be sufficient for its intended use. |
| 🔐 | **Security**       | The codebase does not implement any specific measures to protect data or ensure security. It relies on the user to input their OpenAI API key, and there is a warning message if the key is not provided. However, implementing authentication, encryption, and other security measures would be essential if the codebase were to be deployed in a production environment. |
| 🔀 | **Version Control**| It appears that the codebase is using version control, as it is hosted on GitHub. However, there is no specific information provided about the version control strategies or tools used. Adding information about the branching model, commit conventions, and deployment processes would greatly improve the version control practices. |
| 🔌 | **Integrations**   | The codebase integrates with the OpenAI API to retrieve a list of existing assistants. It also uses the Streamlit library to create a web-based interface for user interaction. The codebase does not have any explicit integrations with other systems or services. |
| 📶 | **Scalability**    | The codebase does not implement

---


## 📂 Repository Structure

```sh
└── AssistantsGPTMngt/
    ├── app.py
    └── requirements.txt

```

---


## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                         | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---                                                                                          | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [requirements.txt](https://github.com/hansipie/AssistantsGPTMngt/blob/main/requirements.txt) | The code in the "requirements.txt" file specifies the dependencies needed for the app in the AssistantsGPTMngt directory to run. These dependencies include "streamlit," "streamlit-file-browser," and "openai.                                                                                                                                                                                                                                                                                                                                    |
| [app.py](https://github.com/hansipie/AssistantsGPTMngt/blob/main/app.py)                     | The code above is for an Assistants Management application. It uses the Streamlit library to create a web-based interface. It allows the user to input their OpenAI API key and provides a sidebar with a reload button. If the API key is not provided, a warning message is displayed and the program stops. It then uses the OpenAI library to retrieve a list of existing assistants and displays them in a tabular format. The user can select assistants for deletion using checkboxes and click a button to delete the selected assistants. |

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ python 3.10`

`- ℹ️ python module: streamlit`

`- ℹ️ python module: openai`

### 🔧 Installation

1. Clone the AssistantsGPTMngt repository:
```sh
► git clone https://github.com/hansipie/AssistantsGPTMngt
```

2. Change to the project directory:
```sh
► cd AssistantsGPTMngt
```

3. Create the secret file containing your OpenAI API key (optionnal)
```sh
► echo "OPENAI_API_KEY = \"sk-******\"" >> .streamlit/secrets.toml
```
> [!NOTE]
> - NB: This simply set the environment variable at streamlit's runtime. It the API key is not provided as described here, the environment variable will have to be set manually:
>
>   On `Linux/MacOS`
>   ```bash
>   export OPENAI_API_KEY=YOUR_API_KEY
>   ```
>   On `Windows`
>   ```bash
>   set OPENAI_API_KEY=YOUR_API_KEY
>   ```
> 
> - NB2: If the API key is not provided in the environment it will have to be set in the UI

4. Install the dependencies:
```sh
► pip install -r requirements.txt
```

### 🤖 Running AssistantsGPTMngt

From `CLI`

```sh
► streamlit run app.py
```

Using `Docker`
```sh
► docker compose up
```

Using `Streamlit`

Try <em>AssistantGPTMngt</em> in your browser, no installation required!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://assistantsgptmngt.streamlit.app/)

> [!NOTE]
>
> Hosted on Streamlit's Community Cloud. It may be unstable or unavailable at times.

---


## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/hansipie/AssistantsGPTMngt/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/hansipie/AssistantsGPTMngt/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/hansipie/AssistantsGPTMngt/issues)**: Submit bugs found or log feature requests for HANSIPIE.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License


This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---

