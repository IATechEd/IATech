# IATechED Website

Welcome to the IATechED website repository! This project contains the official site of our club, showcasing our achievements, members, and projects. If you're looking to understand how the website works or want to contribute, you've come to the right place.

## Project Overview

The website is built using HTML, vanilla JavaScript, and TailwindCSS. The content on the site is dynamically rendered by passing JSON objects to the JavaScript files, which then display the appropriate information on the site.

### Technologies Used

| Technology Used | Purpose |
| --------------- | ------- |
| HTML            | Provides structure and text for the website. |
| Javascript (vanilla) | Handles dynamic content rendering and minor scripting. |
| Tailwind CSS    | Provides design and color choices. |

## Directory Structure

- `index.html`: The main webpage file, what appears when you open iateched.org.
- `/html/`: This directory contains the subpages, which render all of the content not contained on the main webpage.
- `/bytejam/`: This directory it contains our work for Bytejam 202X, a time travel simulation which won the student's choice award. 
- `/guide/`: This directory contains a list of small security changes anyone can make to enhance their online safety, written by our members.
- `/theprivacyplaybook`: In Progress
- `/static/`: This directory contains all static assets for the website such as images and links.
    - `/json/`: This directory contains all the JSON files used to store the content displayed on the website.
    - `/images/`: This directory contains all of the images in our website, including logos and profile pictures. 

## How It Works

The website's content is managed through JSON files located in the `/static/json/` directory. These JSON files include information about members, achievements, projects, and more. When the website loads, the JavaScript fetches this data and displays it on the relevant sections of the site.

## How to Contribute

We welcome contributions to improve the website! You can contribute by modifying the JSON files to update or add content. Here’s how you can do it:

1. **Fork this repository** to your GitHub account.
2. **Clone your fork** to your local machine.
3. **Navigate to the `JSON/` directory** and edit the relevant JSON file to:
	- Add yourself as a member.
	- Add an achievement.
	- Add a project.
	- Make any other necessary changes.
4. **Commit your changes** and push them to your fork.
5. **Create a Pull Request (PR)** to propose your changes to this repository.

Once your PR is reviewed and approved, your changes will be merged, and the website will be updated accordingly.

## Contact

If you have any questions or need help with contributing, feel free to reach out to the IATechED team at [centraliowacyber@gmail.com](mailto:centraliowacyber@gmail.com).

Happy coding!
