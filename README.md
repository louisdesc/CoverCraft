# CoverCraft - Cover Letter Automation Script

This script is designed to automate the process of generating cover letters for job applications. It integrates with the OpenAI API to create personalized letters by matching the job description with the applicant's profile.

## Features

- Reads job and profile information from text files.
- Utilizes the OpenAI API to generate a customized cover letter.
- Extracts and cleans the generated data to fit a specific letter format.
- Exports the finalized cover letter to a text file, named according to the job position and company.

## Prerequisites

To run this script, you need to have Python installed on your machine. Additionally, the `openai` Python package must be installed and configured with your OpenAI API key.

## Setup

1. **Environment Variable:**
   - Ensure that the `OPENAI_API_KEY` environment variable is set to your OpenAI API key. This is crucial for the script to interact with the OpenAI API.

2. **Installation:**
   - If not already installed, you can install the `openai` package using pip:
     ```
     pip install openai
     ```

## Usage

1. **Prepare Input Files:**
   - Place `job_info.txt`, `profile_info.txt`, and `letter_raw.txt` in the same directory as the script. These files should contain the job description, your profile information, and the raw format for the cover letter, respectively.

2. **Run the Script:**
   - Execute the script in a Jupyter notebook or any Python interpreter. The script is divided into sections for easy understanding and modification.

3. **Review and Export:**
   - The script will generate a cover letter based on the inputs and export it to a text file named after the job position and company.

## Input File Formats

- **job_info.txt:** Should contain the job description.
- **profile_info.txt:** Should include details about your skills and experiences.
- **letter_raw.txt:** Must have the template or format you wish the cover letter to follow.

## Output

- The script exports the generated cover letter to a text file, formatted as `CL/CL - [Position] - [Company].txt`, where `[Position]` and `[Company]` are extracted from the processed data.

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