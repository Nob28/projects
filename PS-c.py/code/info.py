import os
import json

def ask(question):
    answer = input(f"{question}:").strip()
    return answer if answer else None





def main():

    print('\n _____________________________________________________________\n \n')
    print('---info on the person--- \n')
    
    target_id = ask("The target ID")
    if not target_id:
        print('You must enter the target name')
        return
    

    info = {}

    print('\n Add questions and information about the victim. Type "Done" to stop the entry.\n')
    while True:
        
        question = ask('Question \n')
        if question is None or question.lower() in ['done' , 'exit']:
            break
        answer = ask('Answer \n')
        info[question] = answer if answer else None
    
    target_file = f'data/{target_id}.json'
    with open(target_file, "w" ) as f:
        json.dump(info , f, indent=4 , ensure_ascii=False)
    print(f"Done the file {target_file}")

main()