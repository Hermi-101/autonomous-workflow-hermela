import pandas as pd 
import json
from utills import get_db_connection


def load_anchored_data():
    conn = get_db_connection()
    query = """
    SELECT 
       c.id_employee, c.timestamp, c.image_path,
       e.app_name, e.window_title, e.event, e.url
    FROM captures c 
    JOIN events e on c.event_id = e.id
    ORDER BY c.id_employee, c.timestamp
    """

    df = pd.read_sql(query, conn)
    conn.close()
    df["timestamp"] = pd.to_datetime(df["timestamp"], format ='ISO8601')
    df["date"] = df["timestamp"].dt.date.astype(str)
    return df


def get_workflow_signature(sequence):
    """ Creates a unique string for a sequence of action to identify repetitions"""
    return "->".join([f"{row['app_name']}:{row['event']}"for _, row in sequence.iterrows()])


def process_task_1():
    df = load_anchored_data()
    all_extracted_workflows = []


    #Process each employee independently
    for emp_id in df["id_employee"].unique():
        emp_df = df[df["id_employee"] == emp_id].copy()


        window_size = 5
        patterns = {}
        for i  in range(len(emp_df) - window_size + 1):
            window = emp_df.iloc[i: i + window_size]
            signature = get_workflow_signature(window)
            date = window.iloc[0]["date"]

            if signature not in patterns:
                patterns[signature] = {
                    "steps": window.to_dict('records'),
                    "dates":set()

                }

            patterns[signature]["dates"].add(date)
            
        for sig, data in patterns.items():
            dates_active = list(data["dates"])
            num_days = len(dates_active)


            if num_days >= 1:
                workflow_entry = {
                    "employee_id":emp_id,
                    "pattern_signature":sig,
                    "persistence":{
                        "daily_count": num_days,
                        "is_2day": num_days>=2,
                        "is_3day": num_days>=3,
                        "is_4day": num_days>=4
                    },
                    "steps":data["steps"]
                }

                all_extracted_workflows.append(workflow_entry)

    with open("../workflow.json","w") as f:
        json.dump(all_extracted_workflows, f, indent=4, default=str)

    print(f"Task 1 Complete: Found{len(all_extracted_workflows)} unique patterns.")

if __name__ == "__main__":
    process_task_1()                   

               
