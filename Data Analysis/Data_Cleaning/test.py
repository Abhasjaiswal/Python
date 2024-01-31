import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_emails = person[person.duplicated('email', keep=False)]['email'].drop_duplicates()

    result_df = pd.DataFrame({'Email': duplicate_emails})

    return result_df

person_data = {'id': [1, 2, 3],
               'email': ['a@b.com', 'c@d.com', 'a@b.com']}

person_df = pd.DataFrame(person_data)

result_df = duplicate_emails(person_df)
print(result_df)