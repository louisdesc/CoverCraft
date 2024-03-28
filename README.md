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

- The script exports the generated cover letter to a text file, formatted as `CL - [Position] - [Company].txt`, where `[Position]` and `[Company]` are extracted from the processed data.

## Note

This script demonstrates the use of the OpenAI API for generating content based on specific inputs. The quality of the output depends on the input data and the template provided. It may require manual adjustments for optimal results.

