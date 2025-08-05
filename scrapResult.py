import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_student_result(roll_number):
    url = f"https://results.ietdavv.edu.in/DisplayStudentResult?rollno={roll_number}&typeOfStudent=Regular"

    try:
        print(f"Fetching result for roll number: {roll_number}...")
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        student_data = []
        all_tables = soup.find_all('table')
        if len(all_tables) < 6:
            return [f"Not found or result not declared for: {roll_number}"]

        name_table = all_tables[3]
        for row in name_table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1 and cells[1].find('b'):
                value = cells[1].find('b').text.strip()
                student_data.append(value)

        result_table = all_tables[5]
        for row in result_table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1:
                label = cells[1].text.strip()
                student_data.append(label)

        if not student_data:
             return [f"Could not parse data for: {roll_number}"]

        return student_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching result for {roll_number}: {e}")
        return [f"Error fetching: {roll_number}"]
    except Exception as e:
        print(f"An unexpected error occurred for {roll_number}: {e}")
        return [f"Error parsing: {roll_number}"]


if __name__ == "__main__":

    headers = ["Name", "Enrollment No.", "Roll No", "SGPA", "Result"]
    all_student_records = []
    
    a = 4000
    roll_number_batches = {
        "23C": range(1, 190),
        "23I": range(1, 190),
        "23E": range(1,100),
        "23V": range(1,60),
        # "23E": range(1,100),
    }

    for prefix, num_range in roll_number_batches.items():
        for i in num_range:
            roll_number = f"{prefix}{a + i}"
            s_data = get_student_result(roll_number)
            if "Not found" in s_data[0] or "Error" in s_data[0]:
                error_row = [s_data[0]] + [""] * (len(headers) - 1)
                all_student_records.append(error_row)
            else:
                all_student_records.append(s_data)

    df = pd.DataFrame(all_student_records, columns=headers)
    output_filename = "student_results.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Successfully saved results to {output_filename}")