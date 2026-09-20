import pandas as pd
from config import DATA_PATH


def extract_data():

    patients = pd.read_csv(
        DATA_PATH + "patient_registration.csv"
    )

    appointments = pd.read_csv(
        DATA_PATH + "appointments.csv"
    )

    lab_reports = pd.read_csv(
        DATA_PATH + "laboratory_reports.csv"
    )

    wearable = pd.read_csv(
        DATA_PATH + "wearable_health_readings.csv"
    )

    consultations = pd.read_csv(
        DATA_PATH + "doctor_consultations.csv"
    )

    print("Data extraction completed successfully.")

    print("Patients:", len(patients))
    print("Appointments:", len(appointments))
    print("Lab Reports:", len(lab_reports))
    print("Wearable Readings:", len(wearable))
    print("Consultations:", len(consultations))

    return (
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations
    )



# Step 1: Data Extraction

# The extraction stage collects data from multiple hospital source systems.

# In this project, the source systems are represented by five CSV files:

# Patient registration
# Appointment scheduling
# Laboratory reports
# Wearable health devices
# Doctor consultations

# Pandas `read_csv()` is used to load the CSV files into DataFrames.

# The function returns all five DataFrames so that they can be processed during the transformation stage.

# This represents the **Extract** phase of the ETL pipeline.