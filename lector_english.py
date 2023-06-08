import pandas as pd

def transform_csv_to_text(file):
    df = pd.read_csv(file)
    formatted_text = ''

    for index, row in df.iterrows():
        formatted_text += f'## {row["Name (as you want it to be published)"]}\n'
        formatted_text += '**Could you introduce yourself briefly? What do you do and what are your hobbies?:**\n' + f'{row["Could you introduce yourself briefly? What do you do and what are your hobbies?"]}\n\n'
        formatted_text += '**What exactly will you talk about in your talk/workshop? Why did you choose that topic?:**\n' + f'{row["What exactly will you talk about in your talk/workshop? Why did you choose that topic?"]}\n\n'
        formatted_text += '**What would you like to achieve by connecting with the audience with the talk/workshop?:**\n' + f'{row["What would you like to achieve by connecting with the audience with the talk/workshop?"]}\n\n'
        formatted_text += '**What is your favorite programming language?:**\n' + f'{row["What is your favorite programming language?"]}\n\n'
        formatted_text += '**What is your favorite editor or programming environment?:**\n' + f'{row["What is your favorite editor or programming environment?"]}\n\n'
        formatted_text += '**What free software project you couldn\'t live without would you recommend?:**\n' + str(row["What free software project you couldn't live without would you recommend?"]) + '\n\n'
        formatted_text += '**What was your first experience with free software/hardware?:**\n' + f'{row["What was your first experience with free software/hardware?"]}\n\n'
        formatted_text += '**What was your first contact with free software/hardware?:**\n' + f'{row["What was your first contact with free software/hardware?"]}\n\n'
        formatted_text += '**Do you contribute to free software/hardware? If yes: What is your main motivation for doing so?:**\n' + f'{row["Do you contribute to free software/hardware? If yes: What is your main motivation for doing so?"]}\n\n'
        formatted_text += '**In your opinion, what is the best way to start contributing to an open project?:**\n' + f'{row["In your opinion, what is the best way to start contributing to an open project?"]}\n\n'
        formatted_text += '**Is it your first time in OpenSouthCode? If yes: How did you get to know us?:**\n' + f'{row["Is it your first time in OpenSouthCode? If yes: How did you get to know us?"]}\n\n'
        formatted_text += '**And finally, a little-known detail about you from your childhood: your favorite toy, what did you like to break, did you eat well or were a pain at the table... Tell us your story.:**\n' + f'{row["And finally, a little-known detail about you from your childhood: your favorite toy, what did you like to break, did you eat well or were a pain at the table... Tell us your story."]}\n\n' 

    return formatted_text

file = 'Interview with speakers (Responses).csv' #cambia el nombre al que quieras como fichero de entrada.

# Aquí escribimos el contenido en un archivo Markdown
with open('EntrevistasIngles.md', 'w') as f: # cambia el nombre que quieras como fichero de salida.
    f.write(transform_csv_to_text(file))


