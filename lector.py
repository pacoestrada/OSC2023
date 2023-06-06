import pandas as pd

def transform_csv_to_text(file):
    df = pd.read_csv(file)
    formatted_text = ''

    for index, row in df.iterrows():
        formatted_text += f'## {row["Nombre (tal y como quieres que se publique)"]}\n'
        formatted_text += '**¿Podrías presentarte brevemente? ¿A qué te dedicas y cuáles son tus aficiones?:**\n' + f'{row["¿Podrías presentarte brevemente? ¿A qué te dedicas y cuáles son tus aficiones?"]}\n\n'
        formatted_text += '**¿De qué hablarás exactamente en tu charla/taller? ¿Por qué elegiste ese tema?:**\n' + f'{row["¿De qué hablarás exactamente en tu charla/taller? ¿Por qué elegiste ese tema?"]}\n\n'
        formatted_text += '**¿Qué te gustaría conseguir al conectar con la audiencia con la charla/taller?:**\n' + f'{row["¿Qué te gustaría conseguir al conectar con la audiencia con la charla/taller?"]}\n\n'
        formatted_text += '**¿Cuál es tu lenguaje de programación favorito?:**\n' + f'{row["¿Cuál es tu lenguaje de programación favorito?"]}\n\n'
        formatted_text += '**¿cual es tu editor/IDE favorito?:**\n' + f'{row["¿cual es tu editor/IDE favorito?"]}\n\n'
        formatted_text += '**¿Qué proyecto de software libre sin el que no podrías vivir recomendarías?:**\n' + f'{row["¿Qué proyecto de software libre sin el que no podrías vivir recomendarías?"]}\n\n'
        formatted_text += '**¿Contribuyes al software/hardware libre? En caso afirmativo: ¿Cuál es tu principal motivación para hacerlo?:**\n' + f'{row["¿Contribuyes al software/hardware libre? En caso afirmativo: ¿Cuál es tu principal motivación para hacerlo?"]}\n\n'
        formatted_text += '**¿Es tu primera vez en OpenSouthCode? En caso afirmativo: ¿Cómo llegaste a conocernos?:**\n' + f'{row["¿Es tu primera vez en OpenSouthCode? En caso afirmativo: ¿Cómo llegaste a conocernos?"]}\n\n'
        formatted_text += '**Y ya para terminar, un detalle poco conocido sobre ti de tu infancia: tu juguete favorito, qué te gustaba romper, comías bien o eras un dolor en la mesa... Cuéntanos tu historia.:**\n' + f'{row["Y ya para terminar, un detalle poco conocido sobre ti de tu infancia: tu juguete favorito, qué te gustaba romper, comías bien o eras un dolor en la mesa... Cuéntanos tu historia."]}\n\n'

    return formatted_text

file = 'Entrevistas a ponentes (Responses).csv'

# Here we write the content to a markdown file
with open('Entrevistas.md', 'w') as f:
    f.write(transform_csv_to_text(file))

