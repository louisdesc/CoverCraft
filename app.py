import os,json
from openai import OpenAI

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def create_openai_completion(model, messages):
    from openai import OpenAI
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature= 0.15,
            response_format={ "type": "json_object" }
        )
        return completion
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def prepare_messages(profile_info, job_info, letter_format):
    return [
        {"role": "system", "content": "Je suis un assistant qui permet de remplir les lettres de motivation pour vos candidatures. Je fais le lien entre vos expériences, vos compétences et l'offre d'emploi. Le schema JSON doit contenir : Entreprise, Poste, Objet, Contenu"},
        {"role": "user", "content": f"Voici mes compétences et expériences : {profile_info}"},
        {"role": "system", "content": "Donnez moi l'offre d'emploi."},
        {"role": "user", "content": f"Voici le contenu de l'offre d'emploi : {job_info}"},
        {"role": "system", "content": "Donne moi le format type de lettre de motivation que je dois suivre."},
        {"role": "user", "content": f"Voici le format type de contenu que j'aimerais que tu suives : {letter_format}"},
    ]


def process_job_application(profile_info, letter_raw, job_info_filename):
    """Processes a single job application."""
    job_info = read_file(job_info_filename)
    job_name = os.path.splitext(os.path.basename(job_info_filename))[0]
    print(f"Processing: {job_name}")
    
    messages = prepare_messages(profile_info, job_info, letter_raw)
    # completion = create_openai_completion("gpt-4-0125-preview", messages)
    completion = create_openai_completion("gpt-3.5-turbo-0125", messages)
    

    if completion:
        result_raw = json.loads(completion.choices[0].message.content)
        # print(result_raw) # DEBUG

        # Prepare export content
        link_to_the_job = job_info[0]
        export_content = f"{link_to_the_job}\n\n{result_raw['Objet']}\n{result_raw['Contenu']}"
        
        num_file = job_info_filename[9:-4] # Remove job_info_ and .txt
        # Define export path
        file_path = f"CL/{result_raw['Entreprise']} - {num_file} - {result_raw['Poste'].replace('/', '-')}.txt"

        
        # Write the content to file
        with open(file_path, "w", encoding='utf-8') as file:
            file.write(export_content)
        print(f"Exported to {file_path}")
    else:
        print("Failed to get a response from the OpenAI API.")
    print("============================================\n")

def process_all_jobs(jobs_directory, profile_info, letter_raw):
    """Processes all job applications in a directory."""
    for filename in os.listdir(jobs_directory):
        if filename.startswith("job_info_") and filename.endswith(".txt"):
            job_info_filename = os.path.join(jobs_directory, filename)
            # print(job_info_filename) # DEBUG
            
            process_job_application(profile_info, letter_raw, job_info_filename)

def main():
    data_directory = "data" 
    profile_info_path = os.path.join(data_directory, "profile_info.txt")
    letter_raw_path = os.path.join(data_directory, "letter_raw.txt")
    jobs_directory = os.path.join(data_directory, "jobs")
    
    # Read the common files
    profile_info = read_file(profile_info_path)
    letter_raw = read_file(letter_raw_path)
    
    # Process all job applications
    process_all_jobs(jobs_directory, profile_info, letter_raw)

if __name__ == "__main__":
    main()