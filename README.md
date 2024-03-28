# CoverCraft - Cover Letter Automation Script

CoverCraft streamlines the process of creating personalized cover letters for job applications by leveraging the power of OpenAI's GPT models. It automatically matches the applicant's profile with job descriptions to generate tailored cover letters, enhancing your job application process.

## Features

- **Automated Customization:** Generates cover letters that align the applicant's skills and experiences with job descriptions.
- **OpenAI Integration:** Utilizes OpenAI's GPT models for intelligent text generation and customization.
- **Multi-Job Processing:** Supports processing multiple job applications, creating individual cover letters for each.
- **Dynamic Template Usage:** Adapts a user-defined cover letter template to fit the specifics of each job application.
- **Simplified File Management:** Organizes job descriptions, profile information, and output cover letters in a structured directory.

## Prerequisites

- **Python:** Ensure Python is installed on your system.
- **OpenAI API Key:** An OpenAI API key is required to access the GPT models.

## Setup

1. **Environment Variable:**
   - Ensure that the `OPENAI_API_KEY` environment variable is set to your OpenAI API key. This is crucial for the script to interact with the OpenAI API.

2. **Installation:**
   - If not already installed, you can install the `openai` package using pip:
     ```
     pip install openai
     ```

## Project Structure

This project is organized to facilitate easy management of input files and output cover letters. Below is an overview of the key directories and files:

- **`data/` Directory:** Serves as the root folder for input and template files.
  - **`jobs/` Subdirectory:** Contains individual text files for each job description. File names should start with `job_info_` and end with `.txt` to be recognized by the script.
  - **`profile_info.txt`:** A single file that holds the applicant's skills, experiences, and any other relevant information.
  - **`letter_raw.txt`:** Defines the cover letter template. This file should outline the desired structure and content format for the generated letters.

## How to Use

Follow these steps to prepare your application materials and run the script:

1. **Prepare Your Materials:**
   - Populate the `data/jobs/` directory with text files for each job you're applying to. Each file should contain the job description and title.
   - Update `data/profile_info.txt` with your personal profile, including skills, experiences, and achievements relevant to your job search.
   - Customize the cover letter format in `data/letter_raw.txt` to match your preferred style and structure.

2. **Run the Script:**
   - Execute the main script. It will process each job description in the `data/jobs/` directory, using your profile information and the template from `letter_raw.txt` to generate tailored cover letters.

3. **Review and Distribute:**
   - Generated cover letters will be saved in the `CL/` directory, named after the target company and position. Review each letter for personal touches before sending.

## Output Details

The script generates and stores each cover letter in a structured format within the `CL/` directory. The naming convention is `[Company] - [Position].txt`, making it straightforward to locate and review letters for specific applications.

## Example Result
https://bouyguestelecom-recrute.talent-soft.com/offre-de-emploi/emploi-alternance-developpeur-ia-test-f-h_47683.aspx


Objet : Candidature pour une alternance en Développeur IA/Test F/H chez Bouygues Telecom

Madame, Monsieur,

Actuellement en préparation d'un Master 2 spécialisé en Big Data & Machine Learning à l'Efrei, je suis activement à la recherche d'une entreprise pour m'accueillir un an à partir d’octobre 2024. Cette expérience sera l’occasion d’enrichir ma formation théorique par une expérience pratique. C'est avec beaucoup d'enthousiasme que je vous présente ma candidature pour une alternance chez Bouygues Telecom pour le poste de Développeur IA/Test F/H.

Votre entreprise est reconnue pour son engagement dans l'innovation technologique et l'excellence de ses services dans le domaine des télécommunications. Je suis particulièrement intéressé par votre approche d'intégration de l'intelligence artificielle pour améliorer et optimiser les processus, ce qui représente une opportunité inestimable de contribuer à des projets d'avant-garde.

En tant que candidat passionné par les technologies de pointe, notamment en matière d'intelligence artificielle et de big data, je suis convaincu que cette alternance chez Bouygues Telecom me permettra de découvrir de nouvelles techniques et de travailler avec des professionnels expérimentés dans le domaine des systèmes d'informations. Je suis également conscient des défis inhérents à la mise en place et au développement d'interfaces utilisateur conviviales et de mécanismes de collecte de données efficaces pour le traitement du langage naturel.

Mes compétences techniques, acquises au fil de mes expériences dans le développement d'applications permettant la transformation de CV en données structurées, l'automatisation des processus via Dataiku et la manipulation de Python pour divers projets, correspondent étroitement aux besoins de votre poste. La mise en œuvre de solutions cloud avec AWS, l'exploitation de Data Science et de Machine Learning pour l'analyse de données et mon intérêt pour les techniques avancées de traitement du langage naturel (NLP) mettent en avant ma capacité à contribuer au succès de vos projets en matière d'IA et de tests.

Je serais honoré de pouvoir apporter mon dynamisme, ma créativité et mon expertise au sein de Bouygues Telecom et j'espère que ma candidature retiendra votre attention. Je suis convaincu que cette alternance serait une expérience professionnelle très enrichissante pour moi et que je pourrais contribuer de manière significative à vos projets d'innovation.

Je vous remercie pour l'attention que vous porterez à ma candidature et je suis à votre disposition pour toute information complémentaire ou pour un entretien.

Cordialement,

Louis DESCLOUS