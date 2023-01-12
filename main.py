import os

def main():
    init_session_path = os.path.join(os.getcwd(), "main", "init_session.py")
    get_data_path = os.path.join(os.getcwd(), "main", "get_data.py")
    json_excel_path = os.path.join(os.getcwd(), "main", "json_to_excel.py")

    if os.path.isfile(init_session_path) and os.access(init_session_path, os.R_OK):
        with open(init_session_path, 'r') as f:
            exec(f.read())
    else:
        print(f"{init_session_path} not found or not accessible")

    if os.path.isfile(get_data_path) and os.access(get_data_path, os.R_OK):
        with open(get_data_path, 'r') as f:
            exec(f.read())
    else:
        print(f"{get_data_path} not found or not accessible")
    
    if os.path.isfile(json_excel_path) and os.access(json_excel_path, os.R_OK):
        with open(json_excel_path, 'r') as f:
            exec(f.read())
    else:
        print(f"{json_excel_path} not found or not accessible")

if __name__ == "__main__":
    main()
